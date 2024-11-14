import time
from socket import *

# Set server address and port
server_address = '127.0.0.1'  # Localhost for testing
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

# Set a timeout of 1 second for responses
client_socket.settimeout(1)

# Ping the server 10 times
for sequence_number in range(1, 11):
    # Prepare the message with current time
    send_time = time.time()
    message = f"Ping {sequence_number} {send_time}"

    try:
        # Send the message to the server
        client_socket.sendto(message.encode(), (server_address, server_port))

        # Record the time the response is received
        received_message, server = client_socket.recvfrom(1024)
        receive_time = time.time()

        # Calculate round-trip time (RTT)
        rtt = receive_time - send_time

        # Print the server's response and RTT
        print(f"Reply from server: {received_message.decode()}")
        print(f"Round-Trip Time (RTT): {rtt:.6f} seconds")

    except timeout:
        # If no response within 1 second, assume packet loss
        print("Request timed out")

# Close the socket
client_socket.close()