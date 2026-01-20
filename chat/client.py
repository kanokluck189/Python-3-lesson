import socket
from threading import Thread
import time

HOST = "127.0.0.1"
PORT = 21001


def poller(sock):
    while True:
        time.sleep(2)
        try:
            sock.send("POLL".encode())
            data = sock.recv(4096)
            if data:
                print("\n[SERVER]")
                print(data.decode())
        except:
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CONNECTED]")

    Thread(target=poller, args=(s,), daemon=True).start()

    while True:
        msg = input("Enter message (or exit): ")
        if msg.lower() == "exit":
            break

        s.send(f"SEND:{msg}".encode())

print("[CLIENT CLOSED]")
# ================= CLIENT END =================