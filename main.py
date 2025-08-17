# this allows us to use code from
# the open-source pygame library
# throughout this file

import sys

import pygame
import player
import constants
import asteroid
import asteroidfield
import shot

def main():

    # Welcome Text #
    print(f"Starting Asteroids!\nScreen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")


    # PyGame Initialization #
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # PyGame Clock
    clock = pygame.time.Clock()
    dt = 0

    # PyGame Group
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids  =  pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    player.Player.containers = (updateable, drawable)
    asteroid.Asteroid.containers = (updateable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updateable)
    shot.Shot.containers = (updateable, drawable, shots)


    # Player Object #
    p1 = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    # AsteroidField Object
    a1 = asteroidfield.AsteroidField()

    # Game Loop #

    game_state = 0
    points = 0
    while(game_state == 0):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Screen
        pygame.Surface.fill(screen, (120,120,120))
    
        # Drawing
        for thing in drawable:
            thing.draw(screen)
            #print(thing)


        # Updating
        updateable.update(dt)

        # Collision Check - Player
        for a in asteroids:
            if (a.collision_check(p1)):
                print(f'you are dead! youve got {points} points')
                sys.exit()

        # Collision Check - Bullet
        for a in asteroids:
            for s in shots:
                if (a.collision_check(s)):
                    a.split()
                    points += 1
                    print(f'asteroid killed! points: {points}')



        # Flip
        pygame.display.flip()

        # Clock
        dt = clock.tick(60) / 1000
        #print(f"current delta: {dt}")
        



if __name__ == "__main__":
    main()
