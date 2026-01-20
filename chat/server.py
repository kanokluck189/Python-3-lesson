import socket
from threading import Thread, Lock

HOST = "0.0.0.0"
PORT = 21001

# ================= GLOBAL STATE =================
next_client_id = 1
clients = {}      # client_id -> socket
messages = []     # global message storage
lock = Lock()


def client_processor(conn, client_id):
    print(f"[START] Client handler for client {client_id}")

    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            text = data.decode().strip()
            print(f"[RECV] {client_id}: {text}")

            # -------- SEND MESSAGE (STORE ONLY) --------
            if text.startswith("SEND:"):
                msg_text = text[5:]

                with lock:
                    receivers = list(clients.keys())
                    receivers.remove(client_id)

                    messages.append({
                        "from": client_id,
                        "text": msg_text,
                        "need_to_send": set(receivers)
                    })

            # -------- POLL FOR MESSAGES --------
            elif text == "POLL":
                outgoing = []

                with lock:
                    for msg in messages:
                        if client_id in msg["need_to_send"]:
                            outgoing.append(
                                f"From {msg['from']}: {msg['text']}"
                            )
                            msg["need_to_send"].remove(client_id)

                if outgoing:
                    conn.send(("\n".join(outgoing)).encode())
                else:
                    conn.send("No new messages for you for now!".encode())

    except ConnectionResetError:
        pass

    finally:
        with lock:
            del clients[client_id]

        conn.close()
        print(f"[DISCONNECT] Client {client_id}")


# ================= SERVER START =================
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("[SERVER] Listening...")

while True:
    conn, addr = server.accept()

    with lock:
        client_id = next_client_id
        next_client_id += 1
        clients[client_id] = conn

    print(f"[CONNECT] Client {client_id} from {addr}")

    Thread(
        target=client_processor,
        args=(conn, client_id),
        daemon=True
    ).start()
# ================= SERVER END =================