class NPC:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self, max_x, max_y):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > max_x:
            self.vx *= -1
        if self.y < 0 or self.y > max_y:
            self.vy *= -1

        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y))
