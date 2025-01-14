import socket  # noqa: F401
import base64

def message(cid, error_code):
    # First have the correlation id in 4 bytes
    payload = cid.to_bytes(4, byteorder="big")
    # Then the error code for the request in 2 bytes
    payload += error_code.to_bytes(2, byteorder="big")
    # total message size will the the size of the payload in bytes and will be stored in the first 4 bytes
    message_size = len(payload).to_bytes(4, byteorder="big")
    return message_size + payload

def parse_request(req): 
    message_size = int.from_bytes( (req[:4]), byteorder='big')
    request_api_key = int.from_bytes( (req[4:6]), byteorder='big')
    request_api_ver = int.from_bytes( (req[6:8]), byteorder='big')
    correlation_id = int.from_bytes( (req[8:12]), byteorder='big')

    print("client reponse had : ")
    print(message_size, request_api_key, request_api_ver, correlation_id)
    return message_size, request_api_key, request_api_ver, correlation_id
    

def handle_client(client):
    client_request = client.recv(1024)
    msg_sz, req_api_key, req_api_ver, corr_id = parse_request(client_request)
    
    # API key will be 18 as the ApiVersionsRequest
    assert req_api_key == 18
    
    error_code = 0 if (req_api_ver == 4)  else 35
    client.sendall(message(corr_id, error_code=error_code))
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
