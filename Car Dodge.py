import pygame
import random
import time

pygame.init()
car_width = 115
car_height = 236
screen_width = 600
screen_height = 700
car_speed = 7


screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()

img = pygame.image.load('car.jpg')


# Generating obstacle
def enemy_generation(enemy_x, enemy_y, radius):
    pygame.draw.circle(screen, (0, 128, 0), (enemy_x, enemy_y), radius)


# checking for collision
def collision(car_x, car_y, enemy_x, enemy_y, radius):
    if enemy_y >= car_y:
        if car_x < enemy_x < car_x + car_width or car_x < enemy_x - radius < car_x + car_width or car_x < enemy_x + radius < car_x + car_width:
            print('\n****** You Collided ******\n')
            return True
    elif car_x < 0 or car_x + car_width > screen_width:
        print('\n****** You Collided ******\n')
        return True
    else:
        return False


# Main game loop
def game_loop():

    # defining basic parameters for game
    car_x = 300
    car_y = 450
    radius = 20
    enemy_x = 20
    enemy_y = 20
    enemy_speed = 5
    score = 0

    while True:

        screen.fill((255, 255, 255))    # making the background white

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('\n****** Game Closed ******\n')
                pygame.quit()
                quit()

        enemy_y += enemy_speed
        enemy_generation(enemy_x, enemy_y, radius)

        if collision(car_x, car_y, enemy_x, enemy_y, radius):
            time.sleep(2)
            game_loop()

        if enemy_y - radius > screen_height:
            enemy_x = random.randrange(radius, screen_width)
            enemy_generation(enemy_x, enemy_y, radius)
            enemy_y = 0
            score += 10
            print('Score: {}'.format(score))
            if score % 50 == 0:
                enemy_speed += 1

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]: car_x += car_speed
        if pressed[pygame.K_LEFT]: car_x -= car_speed

        screen.blit(img, (car_x, car_y))
        pygame.display.flip()
        clock.tick(60)


game_loop()     # calling the game loop function
pygame.quit()
quit()
