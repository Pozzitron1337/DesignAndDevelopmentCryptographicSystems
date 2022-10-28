import ssl
import requests
from cryptography import x509
from cryptography.hazmat.backends import default_backend

addr = 'localhost'
port = 5000

cert = ssl.get_server_certificate((addr, port), ssl_version=2)
print(cert)
certDecoded = x509.load_pem_x509_certificate(str.encode(cert), default_backend())
print(certDecoded)

url = "https://" + addr + ":" + str(port)
print(url)
responce = requests.get(url=url, verify=False)
print(responce.text)