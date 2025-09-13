import pygame
from game import Game
def main():
    # Initialize Pygame
    pygame.init()

    # Create a game instance
    game = Game()

    # Start the game
    game.start_game()

    # Main game loop
    while True:
        game.update()
        game.draw()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()