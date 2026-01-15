import pygame

class PygameGraphics:
    def __init__(self, width=1280, height=720):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Python Game Engine")
        self.clock = pygame.time.Clock()

    def start_frame(self):
        self.screen.fill("black")

    def render_circle(self, x, y, radius, color):
        pygame.draw.circle(
            self.screen,
            pygame.Color(color),
            (int(x), int(y)),
            radius
        )

    def show_frame(self):
        pygame.display.flip()
