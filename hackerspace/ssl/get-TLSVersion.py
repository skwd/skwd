import socket
import ssl
import argparse

def testTLS(HOST,PORT, Version):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    wrappedSocket = ssl.wrap_socket(sock, ssl_version=Version)
    try:
        wrappedSocket.connect((HOST, PORT))
        wrappedSocket.close()
    except:
        return False
    return True


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Test TLS Version')
    parser.add_argument('--host', type=str, default="www.google.ca", help='host to check')
    parser.add_argument('--port', type=int, default=443,help='Port Number')
    args = parser.parse_args()

    HOST, PORT = args.host, args.port
    try:
        socket.gethostbyname(HOST)
        print("Testing {0} ({1})".format(HOST,PORT))
        if (testTLS(HOST,PORT,ssl.PROTOCOL_TLSv1_2)):
            print("[+]TLS1.2 supported it's PERFECT")
        if (testTLS(HOST,PORT,ssl.PROTOCOL_TLSv1_1)):
            print("[+]TLS1.1 supported it's GOOD")
        if (testTLS(HOST,PORT,ssl.PROTOCOL_TLSv1)):
            print("[*]TLS1.0 supported it's boff")
        if (testTLS(HOST,PORT,ssl.PROTOCOL_SSLv3)):
            print("[-]SSLv3  supported it's BAD")
    except Exception  as ex:
        print("oooooo {}".format(ex))
        
