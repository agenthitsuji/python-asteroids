import pygame
import circleshape
import constants

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        print('draw player')

    def rotate(self, dt):
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
            print("button pressed A")

        if keys[pygame.K_d]:
            self.rotate(-dt)
            print("button pressed D")

        if keys[pygame.K_w]:
            self.move(dt)
            print("button pressed W")

        if keys[pygame.K_s]:
            self.move(-dt)
            print("button pressed S")

    def move (self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
