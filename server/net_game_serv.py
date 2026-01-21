import socket
from threading import Thread

from game.characters import Player, NPC
from game.game_field import GameField
from server.server_game_engine import ServerGameEngine


def client_thread(conn, pid, engine):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            actions = eval(data.decode())
            engine.set_player_actions(pid, actions)

            state = engine.get_game_state_data()
            state["self"] = pid

            conn.sendall(str(state).encode())
        except:
            break

    engine.remove_player(pid)
    conn.close()


def main():
    field = GameField(0, 0, 600, 600)
    engine = ServerGameEngine(field, [], [NPC(200, 200)])

    Thread(target=engine.run_game, daemon=True).start()

    s = socket.socket()
    s.bind(("0.0.0.0", 21001))
    s.listen()

    print("[SERVER] Listening...")

    pid = 0
    while True:
        conn, _ = s.accept()
        pid += 1
        engine.add_player(Player(pid, 100, 100))
        Thread(target=client_thread, args=(conn, pid, engine), daemon=True).start()


if __name__ == "__main__":
    main()
