import pygame
from ball import Ball
from paddle import Paddle
from constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Ping Pong')
        self.clock = pygame.time.Clock()
        
        # Create game objects
        self.ball = Ball()
        self.player = Paddle(50)
        self.opponent = Paddle(WINDOW_WIDTH - 50 - PADDLE_WIDTH)
        
        # Initialize font
        self.font = pygame.font.Font(None, 74)

    def start_game(self):
        self.ball.reset()

    def update(self):
        # Handle continuous keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(up=True)
        if keys[pygame.K_s]:
            self.player.move(up=False)
        if keys[pygame.K_UP]:
            self.opponent.move(up=True)
        if keys[pygame.K_DOWN]:
            self.opponent.move(up=False)

        # Move ball
        self.ball.move()

        # Ball collision with paddles
        if self.ball.rect.colliderect(self.player.rect) or self.ball.rect.colliderect(self.opponent.rect):
            self.ball.speed_x *= -1

        # Score points
        if self.ball.rect.left <= 0:
            self.opponent.score += 1
            self.ball.reset()
        if self.ball.rect.right >= WINDOW_WIDTH:
            self.player.score += 1
            self.ball.reset()

        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw game objects
        self.player.draw(self.screen)
        self.opponent.draw(self.screen)
        self.ball.draw(self.screen)
        
        # Draw center line
        pygame.draw.aaline(self.screen, WHITE, (WINDOW_WIDTH//2, 0), (WINDOW_WIDTH//2, WINDOW_HEIGHT))
        
        # Draw scores
        player_score = self.font.render(str(self.player.score), True, WHITE)
        opponent_score = self.font.render(str(self.opponent.score), True, WHITE)
        self.screen.blit(player_score, (WINDOW_WIDTH//4, 20))
        self.screen.blit(opponent_score, (3*WINDOW_WIDTH//4, 20))
        
        pygame.display.flip()