import random
import pygame
import time

pygame.init()

# screen # caption
screen_X = 1000
screen_Y = 600
screen = pygame.display.set_mode((screen_X, screen_Y))
pygame.display.set_caption("Snake_game")

# snake
snake_x = 500
snake_y = 350
height = 10
width = 10
snake_x_change = 0
snake_y_change = 0
speed = 1
fps = 100
clock = pygame.time.Clock()
red = (125, 150, 50)
# snake length
snake_list = []
snake_length = 1
score = 0


def display_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, red, (x[0], x[1], 10, 10))


# food
food_x = random.randint(1 + height, screen_X - width)
food_y = random.randint(1 + height, screen_Y - width)

# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake_y_change = -speed
                snake_x_change = 0
            elif event.key == pygame.K_s:
                snake_y_change = speed
                snake_x_change = 0
            elif event.key == pygame.K_d:
                snake_x_change = +speed
                snake_y_change = 0
            elif event.key == pygame.K_a:
                snake_x_change = -speed
                snake_y_change = 0
    # snake movement
    snake_x += snake_x_change
    snake_y += snake_y_change
    display_snake(snake_list)
    # snake movement
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    # food
    pygame.draw.rect(screen, (255, 50, 25), (food_x, food_y, height, width))
    if abs(food_x - snake_x) < 6 and abs(food_y - snake_y) < 6:
        food_x = random.randint(1 + height, screen_X - width)
        food_y = random.randint(1 + height, screen_Y - width)
        snake_length += 20
        score += 1
    if snake_x >= screen_X - height or snake_x <= 0:
        time.sleep(1)
        running = False
    elif snake_y >= screen_Y - height or snake_y <= 0:
        time.sleep(1)
        running = False
    for x in snake_list[:-1]:
        if x == head:
            time.sleep(1)
            running = False
    pygame.display.update()
    # fps
    clock.tick(fps)
