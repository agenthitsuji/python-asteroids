# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
import player
import constants

def main():

    # Welcome Text #
    print(f"Starting Asteroids!\nScreen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")


    # PyGame Initialization #
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    # PyGame Clock
    clock = pygame.time.Clock()
    dt = 0

    # Player Object #
    p1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    # Game Loop #

    game_state = 0
    while(game_state == 0):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Screen
        pygame.Surface.fill(screen, (120,120,120))
    
        # Player
        p1.draw(screen)
        p1.update(dt)

        # Flip
        pygame.display.flip()

        # Clock
        dt = clock.tick(60) / 1000
        print(f"current delta: {dt}")
        



if __name__ == "__main__":
    main()
