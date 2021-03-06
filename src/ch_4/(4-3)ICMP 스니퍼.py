from socket import *
import os
import struct

#스니퍼는 네트워크 패킷을 훔쳐보는 프로그램임
#스니퍼 테스트를 위해서는 ICMP 프로토콜을 수신하는 방화벽을 열어야함
def parse_ip_header(ip_header):
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads


def parse_icmp_header(icmp_data):
    icmp_headers = struct.unpack("!BBHHH", icmp_data[:8])
    icmp_payloads = icmp_data[8:]
    return icmp_headers, icmp_payloads


def parsing(host):
    # raw socket 생성 및 bind
    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))

    # socket 옵션
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    # promiscuous mode 켜기
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)

    try:
        while True:
            data = sock.recvfrom(65535)
            ip_headers, ip_payloads = parse_ip_header(data[0])
            if ip_headers[6] == 1:  # ICMP Only
                ip_source_address = inet_ntoa(ip_headers[8])
                ip_destination_address = inet_ntoa(ip_headers[9])
                print(f"{ip_source_address} => {ip_destination_address}")
                icmp_headers, icmp_payloads = parse_icmp_header(ip_payloads)
                if icmp_headers[0] == 0:
                    print("Echo Reply")
                elif icmp_headers[0] == 8:
                    print("Echo Request")
                print("icmp_headers => ", icmp_headers)
                print("icmp_payloads => ", icmp_payloads)
                print("==========================")
    except KeyboardInterrupt:  # Ctrl-C key input
        if os.name == "nt":
            sock.ioctl(SIO_RCVALL, RCVALL_OFF)


if __name__ == "__main__":
    host = "192.168.35.172"  
    #에러 발생 시 명령 프롬프트(cmd) 에서 ipconfig 쳐서 나오는 본인 IP 기입하면 됨
    print("START SNIFFING at [%s]" % host)
    parsing(host)

'''
[패킷출력결과]
192.168.35.172의 응답: 바이트=32 시간<1ms TTL=128
192.168.35.172에 대한 Ping 통계:
    패킷: 보냄 = 4, 받음 = 4, 손실 = 0 (0% 손실),
왕복 시간(밀리초):
    최소 = 0ms, 최대 = 0ms, 평균 = 0ms
'''