from pynput import keyboard

class KBPoller:
    def on_press(self, key):
        try:
            ch = key.char.lower()
            self.pressed.add(ch)
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            ch = key.char.lower()
            self.pressed.remove(ch)
        except AttributeError:
            pass

    def __init__(self):
        self.pressed = set()
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        listener.start()


running = True

player_x = 0
player_y = 0
x_max = 10
y_max = 10

def render_state():
    print(f"\rPlayer position: ({player_x}, {player_y})", end="")

def update_game_state(poller):
    global player_x, player_y, running

    if 'w' in poller.pressed and player_y <= y_max - 1:
        player_y += 1
    if 's' in poller.pressed and player_y >= -(y_max - 1):
        player_y -= 1
    if 'a' in poller.pressed and player_x >= -(x_max - 1):
        player_x -= 1
    if 'd' in poller.pressed and player_x <= x_max - 1:
        player_x += 1
    if 'q' in poller.pressed:
        running = False


poller = KBPoller()

while running:
    update_game_state(poller)
    render_state()
