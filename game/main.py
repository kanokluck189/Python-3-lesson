from game.game_engine import GameEngine
from game.graphics_engine import PygameGraphics
from game.player import Player
from game.npc import NPC

def main():
    graphics = PygameGraphics()

    player = Player(640, 360)

    npcs = [
        NPC(200, 200, 3, 2),
        NPC(800, 300, -2, 3),
        NPC(400, 500, 2, -3),
    ]

    game = GameEngine(
        player=player,
        npcs=npcs,
        graphics=graphics,
        width=1280,
        height=720,
        fps=60
    )

    game.run()

if __name__ == "__main__":
    main()
