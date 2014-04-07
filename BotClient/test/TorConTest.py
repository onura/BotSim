import socket
import socks
import httplib

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

def monkey_patch_socket():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1",9050,True)
    socket.socket = socks.socksocket
    socket.create_connection = create_connection

def main():
    monkey_patch_socket()
    print("Tor is ready.")
    conn = httplib.HTTPConnection("4kh2ktfoq3sp6bjc.onion", 80)
    conn.request("GET","/")
    response = conn.getresponse()
    print(response.read())


if __name__ == "__main__":
    main()