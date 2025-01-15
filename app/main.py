import socket  
from dataclasses import dataclass
from enum import Enum, unique

@unique
class ErrorCode(Enum):
    NONE = 0
    UNSUPPORTED_VERSION = 35
@dataclass
class KafkaRequest:
    msg_size: int
    api_key: int
    api_version: int
    correlation_id: int
    @staticmethod
    def from_client(client: socket.socket):
        data = client.recv(2048)
        return KafkaRequest(
            msg_size=int.from_bytes(data[:4], byteorder='big'),
            api_key=int.from_bytes(data[4:6], byteorder='big'),
            api_version=int.from_bytes(data[6:8], byteorder='big'),
            correlation_id=int.from_bytes(data[8:12], byteorder='big'),
        )

def make_response(request: KafkaRequest):
    response_header = request.correlation_id.to_bytes(4, byteorder='big')
    valid_api_versions = [0, 1, 2, 3, 4]
    error_code = (
        ErrorCode.NONE
        if request.api_version in valid_api_versions
        else ErrorCode.UNSUPPORTED_VERSION
    )
    min_version, max_version = 0, 4
    throttle_time_ms = 0
    tag_buffer = b"\x00"
    response_body = (
        error_code.value.to_bytes(2, byteorder='big')
        + int(2).to_bytes(1, byteorder='big')
        + request.api_key.to_bytes(2, byteorder='big')
        + min_version.to_bytes(2, byteorder='big')
        + max_version.to_bytes(2, byteorder='big')
        + tag_buffer
        + throttle_time_ms.to_bytes(4, byteorder='big')
        + tag_buffer
    )
    response_length = len(response_header) + len(response_body)
    return int(response_length).to_bytes(4, byteorder='big') + response_header + response_body

# def message(cid, error_code):
#     # First have the correlation id in 4 bytes
#     payload = cid.to_bytes(4, byteorder="big")
#     # Then the error code for the request in 2 bytes
#     payload += error_code.to_bytes(2, byteorder="big")
#     # total message size will the the size of the payload in bytes and will be stored in the first 4 bytes
#     message_size = len(payload).to_bytes(4, byteorder="big")
#     return message_size + payload

# def parse_request(req): 
#     message_size = int.from_bytes( (req[:4]), byteorder='big')
#     request_api_key = int.from_bytes( (req[4:6]), byteorder='big')
#     request_api_ver = int.from_bytes( (req[6:8]), byteorder='big')
#     correlation_id = int.from_bytes( (req[8:12]), byteorder='big')

#     print("client reponse had : ")
#     print(message_size, request_api_key, request_api_ver, correlation_id)
#     return message_size, request_api_key, request_api_ver, correlation_id
    

def handle_client(client):
    # client_request = client.recv(1024)
    client_request = KafkaRequest.from_client(client)

    print(client_request)    

    client.sendall(make_response(client_request))
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
