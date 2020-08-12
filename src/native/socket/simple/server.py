import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port

request_count = 0

print('server started')

s.listen(5)  # Now wait for client connection.
while True:
    request_count += 1
    c, addr = s.accept()  # Establish connection with client.
    print('Got connection from', addr)
    message = 'request_count: ' + str(request_count)
    print('sending message: ', message)
    byte_format = str.encode(message)
    c.send(byte_format)
    c.close()  # Close the connection
