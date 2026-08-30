import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "White", self.position, self.radius, SHOT_RADIUS)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt