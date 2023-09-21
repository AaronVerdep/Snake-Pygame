import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("The Snake")

# Colors
BLUE = (0, 0, 255)  # RGB color for blue
RED = (255, 0, 0)   # RGB color for red
WHITE = (255, 255, 255)  # RGB color for white
BLACK = (0, 0, 0)  # RGB color for black

# Player properties
player_size = 50
player_x = (WIDTH - player_size) // 2
player_y = (HEIGHT - player_size) // 2
player_speed = 3
player_body = [(player_x, player_y)]
player_body_timer = 0  # Timer to control body disappearance

# Direction
direction_x = 0
direction_y = 0

# Apple properties
apple_size = 50
apple_x = random.randint(0, WIDTH - apple_size)
apple_y = random.randint(0, HEIGHT - apple_size)

def spawn_apple():
    """Respawn the apple in a random position."""
    global apple_x, apple_y
    apple_x = random.randint(0, WIDTH - apple_size)
    apple_y = random.randint(0, HEIGHT - apple_size)

# Game over flag
game_over = False

# Timer properties
timer = 20 * 60  # 20 seconds (60 frames per second)
font = pygame.font.Font(None, 72)

# Points
points = 0

# FPS counter
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    direction_x = -player_speed
                    direction_y = 0
                elif event.key == pygame.K_RIGHT:
                    direction_x = player_speed
                    direction_y = 0
                elif event.key == pygame.K_UP:
                    direction_x = 0
                    direction_y = -player_speed
                elif event.key == pygame.K_DOWN:
                    direction_x = 0
                    direction_y = player_speed

    if not game_over:
        # Update player position and body
        player_x += direction_x
        player_y += direction_y
        player_body.insert(0, (player_x, player_y))

        # Check for collision with apple
        if player_x < apple_x + apple_size and player_x + player_size > apple_x and \
           player_y < apple_y + apple_size and player_y + player_size > apple_y:
            spawn_apple()
            points += 1  # Increase points when the player eats an apple

    # Clear the screen (fill with a background color)
    screen.fill(WHITE)

    # Draw the player's body
    for segment in player_body:
        pygame.draw.rect(screen, BLUE, (*segment, player_size, player_size))

    # Draw the apple
    pygame.draw.rect(screen, RED, (apple_x, apple_y, apple_size, apple_size))


    # Draw the points
    points_text = font.render(f"Points: {points}", True, BLACK)
    screen.blit(points_text, (10, 100))

    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)  # Pause for 1 second before closing
        running = False

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()
sys.exit()
