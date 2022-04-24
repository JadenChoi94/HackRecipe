#4-4에 이어서..

from pythonping import ping
from time import sleep

with open("./send_logo.png", "rb") as f:
    while True:
        byte = f.read(1024)
        if byte == b"":  # EOF, Null
            ping("192.168.35.172", verbose=True, count=1, payload=b"EOF")
            break
        ping("192.168.35.172", verbose=True, count=1, payload=byte)
        sleep(0.5)


'''
[실제출력결과]
Reply from 192.168.35.172, 1052 bytes in 0.05ms
Reply from 192.168.35.172, 1052 bytes in 0.04ms
Reply from 192.168.35.172, 1052 bytes in 0.04ms
Reply from 192.168.35.172, 1052 bytes in 0.05ms
Reply from 192.168.35.172, 712 bytes in 0.04ms
Reply from 192.168.35.172, 31 bytes in 0.04ms
'''