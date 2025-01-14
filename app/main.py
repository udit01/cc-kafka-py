import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    
    # while(True): 
    client_socket, client_address = server.accept() # wait for client

    encoding = 'utf-16'
    
    message_size = 1
    corr_id = 7
    header = corr_id
    body = ''

    # response = "%d%d"%(message_size, corr_id)
    # print(response)
    # response = bytes(response, 'utf-32')
    # print(response)
    response = bytes('0', encoding)
    response += bytes('7', encoding)
    # print(response)

    # response = b'0001\n0007'
    client_socket.send(response)

    


if __name__ == "__main__":
    main()
