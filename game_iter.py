running = True

player_x = 0
player_y = 0
x_max = 10
y_max = 10

def scan_keys():
    return input("Enter command (w/a/s/d to move, q to quit): ")

def render_state():
    print(f"Player position: ({player_x}, {player_y})")

def update_game_state(command):
    global player_x, player_y, running
    if command == 'w' and player_y < y_max - 1:
        player_y += 1
    elif command == 's' and player_y > -(y_max - 1):
        player_y -= 1
    elif command == 'a' and player_x > -(x_max - 1):
        player_x -= 1
    elif command == 'd' and player_x < x_max - 1:
        player_x += 1
    elif command == 'q':
        running = False

while running:
    render_state()
    command = scan_keys()
    update_game_state(command)
