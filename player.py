from constants import PLAYER_TURN_SPEED
from constants import LINE_WIDTH
from pygame import Surface
import pygame
from constants import PLAYER_RADIUS
from constants import PLAYER_SPEED
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
    
    def move(self, dt: int) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_vector_with_speed = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_vector_with_speed
    
    def turn(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.turn(-dt)
        if keys[pygame.K_d]:
            self.turn(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
