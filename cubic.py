import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Cube with Arrow Keys")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Cube properties
cube_pos = [WIDTH // 2, HEIGHT // 2]
cube_size = 50

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cube_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        cube_pos[0] += 5
    if keys[pygame.K_UP]:
        cube_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        cube_pos[1] += 5

    # Clear the screen
    screen.fill(BLACK)

    # Draw the cube (as a square for this 2D representation)
    pygame.draw.rect(screen, RED, (cube_pos[0], cube_pos[1], cube_size, cube_size))

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(60)

pygame.quit()
sys.exit()
