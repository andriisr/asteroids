from constants import PLAYER_TURN_SPEED
from constants import LINE_WIDTH
from pygame import Surface
import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Player(CircleShape):
    rotation = 0
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen) -> None:
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)
    
    def turn(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.turn(-dt)
        if keys[pygame.K_d]:
            self.turn(dt)