# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame

from constants import * 

def main():
    pygame.init()
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_state = 0
    while(game_state == 0):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()
