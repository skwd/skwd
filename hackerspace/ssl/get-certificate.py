#Get website certificate in PEM encoding

import ssl,argparse

def getCert(HOST,PORT):
    print (ssl.get_server_certificate((HOST, PORT)))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Test TLS Version')
    parser.add_argument('--host', type=str, default="www.google.ca", help='host to fetch certificate')
    parser.add_argument('--port', type=int, default=443,help='Port Number')
    args = parser.parse_args()
    
    HOST, PORT = args.host, args.port
    getCert(HOST,PORT)