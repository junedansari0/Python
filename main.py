import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
BALL_SPEED = 8
PADDLE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)  # Transparent color

# Get the screen's width and height
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Create the screen in full-screen mode
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Move Wall with Invisible Buttons")

# Create paddles and ball
player_paddle = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 20, 100, 10)
ball = pygame.Rect(SCREEN_WIDTH // 2 - 10, SCREEN_HEIGHT // 2 - 10, 20, 20)

# Ball movement variables
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse's x-coordinate relative to the screen's center
    mouse_x = pygame.mouse.get_pos()[0] - SCREEN_WIDTH // 2

    # Move the player's paddle
    if abs(mouse_x) > 50:  # Deadzone to prevent small mouse movements
        player_paddle.x += PADDLE_SPEED if mouse_x > 0 else -PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # Ball collision with player's paddle
    if ball.colliderect(player_paddle) and ball_speed_y > 0:
        ball_speed_y *= -1

    # Ball out of bounds (game over)
    if ball.top >= SCREEN_HEIGHT:
        running = False

    # Clear the screen
    screen.fill(TRANSPARENT)

    # Draw paddles, ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Control the game's speed
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
