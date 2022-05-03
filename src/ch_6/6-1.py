import whois  # pip install python-whois
import socket

url = "hakhub.net"

try:
    url_info = whois.whois(url)
    ip = socket.gethostbyname(url)
    print("=" * 50)
    print("<< URL Info >>")
    print(url_info)
    ip_info = whois.whois(ip)
    print("=" * 50)
    print("<< IP Info >>")
    print(ip_info)
except whois.parser.PywhoisError:
    print("Unregistered")

'''
whois 에서 dns 또는 ip주소로 검색해 대상의 정보를 얻을 수 잇음(도메인정보)
whois.whois(url)를 통해 ISP(통신사)나 Cloud platform(GCP, AWS, Azure)종류 등을 알아낼 수도 있음

'''