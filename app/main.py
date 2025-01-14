import socket  # noqa: F401
import base64

def message(cid):
    idByte = cid.to_bytes(4, byteorder="big")
    header = len(idByte).to_bytes(4, byteorder="big")
    return header + idByte

def parse_request(req): 
    message_size = int.from_bytes( (req[:4]), byteorder='big')
    request_api_key = int.from_bytes( (req[4:6]), byteorder='big')
    request_api_ver = int.from_bytes( (req[6:8]), byteorder='big')
    correlation_id = int.from_bytes( (req[8:12]), byteorder='big')

    print("client reponse had : ")
    print(message_size, request_api_key, request_api_ver, correlation_id)
    return correlation_id
    

def handle_client(client):
    client_request = client.recv(1024)
    corr_id = parse_request(client_request)
    client.sendall(message(corr_id))
    client.close()

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    
    while True:
        client, addr = server.accept()
        handle_client(client)

    


if __name__ == "__main__":
    main()
