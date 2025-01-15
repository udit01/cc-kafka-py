import socket  
import threading
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
        data = client.recv(8192)
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


def client_loop(client):
    while True:
        client_request = KafkaRequest.from_client(client)
        print(client_request, flush=True)    
        response = make_response(client_request)
        # print(response)
        client.sendall(response)

def main():
    # print("Logs from your program will appear here!")
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    threads = []
    while True: 
        client, addr = server.accept()
        t = threading.Thread(target=client_loop, args=(client))
        threads.append(t)
        t.start()
        print("Serving %d clients.", len(threads), flush=True)
    
    # Good practice while ending
    for t in threads:
        t.join()    


if __name__ == "__main__":
    main()
