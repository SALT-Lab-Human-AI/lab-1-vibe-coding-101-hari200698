import pygame
from constants import *

class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(
            x,
            WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2,
            PADDLE_WIDTH,
            PADDLE_HEIGHT
        )
        self.score = 0

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if not up and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += PADDLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)