import random
from logger import log_event
from constants import ASTEROID_MIN_RADIUS
from constants import LINE_WIDTH
import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "White", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        split1_vector = self.velocity.rotate(angle)
        split2_vector = self.velocity.rotate(-angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split1 = Asteroid(self.position.x, self.position.y, split_radius)
        split2 = Asteroid(self.position.x, self.position.y, split_radius)
        split1.velocity = split1_vector * 1.2
        split2.velocity = split2_vector * 1.2