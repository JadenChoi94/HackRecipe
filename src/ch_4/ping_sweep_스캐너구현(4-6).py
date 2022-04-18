from pythonping import ping
from time import time

#ICMP Echo Request를 이용해서 IP범위를 쓸고 지나가면서 존재하는 호스트를 찾아 내는 것을 Ping Sweep Scan이라고 함
def icmp_scan():
    ip_addresses = ["33.22.143.1", "8.8.8.8", "google.com"]
    for ip_address in ip_addresses:
        print(f"Ping Target => {ip_address}")
        ping(ip_address, timeout=1, count=1, verbose=True)


if __name__ == "__main__":
    begin = time()
    icmp_scan()
    end = time()
    print(f"실행 시간: {end - begin}")


'''
[출력결과]
Ping Target => 33.22.143.1
Request timed out
Ping Target => 8.8.8.8
Reply from 8.8.8.8, 29 bytes in 28.81ms
Ping Target => google.com
Reply from 216.58.220.142, 29 bytes in 78.05ms
실행 시간: 1.1250877380371094
'''