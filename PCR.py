import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DNA Simulation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# DNA Strand dimensions
STRAND_WIDTH, STRAND_HEIGHT = 200, 20
x_position = (SCREEN_WIDTH - STRAND_WIDTH) // 2
y_position_top = (SCREEN_HEIGHT - 2 * STRAND_HEIGHT) // 2
y_position_bottom = y_position_top + STRAND_HEIGHT + 10  # 10px gap between strands

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)

    # Draw DNA strands
    pygame.draw.rect(screen, BLUE, (x_position, y_position_top, STRAND_WIDTH, STRAND_HEIGHT))  # Top strand
    pygame.draw.rect(screen, RED, (x_position, y_position_bottom, STRAND_WIDTH, STRAND_HEIGHT))  # Bottom strand

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()