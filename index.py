import pygame

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Sprites Assignment")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sprite setup
sprite1 = pygame.Rect(100, 150, 50, 50)  # Controlled sprite
sprite2 = pygame.Rect(400, 150, 50, 50)  # Static sprite

# Movement speed
speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls for sprite1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite1.x += speed
    if keys[pygame.K_UP]:
        sprite1.y -= speed
    if keys[pygame.K_DOWN]:
        sprite1.y += speed

    # Draw sprites
    pygame.draw.rect(screen, RED, sprite1)
    pygame.draw.rect(screen, BLUE, sprite2)

    pygame.display.flip()

pygame.quit()