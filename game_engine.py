import pygame
import math
import random

class GameEngine:
    def __init__(self, player, npcs, graphics, width, height, fps=60):
        self.player = player
        self.npcs = npcs
        self.graphics = graphics
        self.width = width
        self.height = height
        self.fps = fps
        self.running = True

    def check_collision(self, a, b, radius=20):
        dx = a.x - b.x
        dy = a.y - b.y
        return math.hypot(dx, dy) < radius * 2

    def update_player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player.y -= self.player.speed
        if keys[pygame.K_s]:
            self.player.y += self.player.speed
        if keys[pygame.K_a]:
            self.player.x -= self.player.speed
        if keys[pygame.K_d]:
            self.player.x += self.player.speed

        self.player.x = max(0, min(self.player.x, self.width))
        self.player.y = max(0, min(self.player.y, self.height))

    def update_npcs(self):
        for npc in self.npcs:
            npc.move(self.width, self.height)

        # NPC vs NPC collision
        for i in range(len(self.npcs)):
            for j in range(i + 1, len(self.npcs)):
                a, b = self.npcs[i], self.npcs[j]
                if self.check_collision(a, b):
                    a.vx, b.vx = -a.vx + random.uniform(-1, 1), -b.vx + random.uniform(-1, 1)
                    a.vy, b.vy = -a.vy + random.uniform(-1, 1), -b.vy + random.uniform(-1, 1)

    def handle_player_collision(self):
        for npc in self.npcs:
            if self.check_collision(self.player, npc):
                npc.vx *= -1
                npc.vy *= -1
                self.player.x -= npc.vx * 5
                self.player.y -= npc.vy * 5

    def render(self):
        self.graphics.start_frame()

        self.graphics.render_circle(self.player.x, self.player.y, 20, "red")
        for npc in self.npcs:
            self.graphics.render_circle(npc.x, npc.y, 20, "blue")

        self.graphics.show_frame()

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update_player()
            self.update_npcs()
            self.handle_player_collision()
            self.render()

            clock.tick(self.fps)

        pygame.quit()
