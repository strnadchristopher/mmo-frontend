# This is a python script for testing a websocket connection to a server, and simulating multiple client connections

import asyncio
import websocket
import threading
import json
import time
def main():
    number_of_clients = 500
    threads = []
    for i in range(0,number_of_clients):
        threads.append(threading.Thread(target=create_new_client_connection, args=(i,)))
    for i in range(0,number_of_clients):
        threads[i].setDaemon(True)
        threads[i].start()
        time.sleep(1)
    while True:
        pass

def create_new_client_connection(client_id):
    print("Starting new connection with client id: " + str(client_id))
    connect_message_object = {
        "client_id" : client_id,
        "request": "Connect"
    }
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:2794")
    ws.send(json.dumps(connect_message_object))

    while True:
        print("[Server]: " + ws.recv())
        message_object = {
            "client_id" : client_id,
            "request": "MoveForward"
        }
        ws.send(json.dumps(message_object))


if __name__ == "__main__":
    main()