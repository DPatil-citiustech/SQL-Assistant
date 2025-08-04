import pygame
import random

pygame.init()
width, height = 400, 400
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake = [(20, 20
dx, dy = 20, 0
food = (100, 100)
score = 0

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -20
            if event.key == pygame.K_DOWN:
                dx, dy = 0, 20
            if event.key == pygame.K_LEFT:
                dx, dy = -20, 0
            if event.key == pygame.K_RIGHT:
                dx, dy = 20, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)
    if head == food:
        score += 1
        food = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
    else:
        snake.pop()

    if head[0] < 0 or head[0] > width or head[1] < 0 or head[1] > height or head in snake[1:]:
        run = False

    win.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(win, (0, 255, 0), (s[0], s[1], 20, 20))
    pygame.draw.rect(win, (255, 0, 0), (food[0], food[1], 20, 20))
    pygame.display.update()
    clock.tick(10)

pygame.quit()