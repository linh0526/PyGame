import pygame
import random

from pygame.locals import *
from pygame import mixer

# Initialize Pygame
pygame.init()

# Set up display
width, height = 440, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Linhpro')

# Set up icon
icon = pygame.image.load(r'assets\img\icon.png')
pygame.display.set_icon(icon)

# Load hình nền
background_image = pygame.image.load(r'assets\img\background.png')

# Set up background music
pygame.mixer.init()
pygame.mixer.music.load(r'assets\sound\music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Load hiệu ứng âm thanh
eat_sound = pygame.mixer.Sound(r'assets\sound\eat.mp3')
over_sound = pygame.mixer.Sound(r'assets\sound\over.mp3')


# Variables
score = 0
highScore = 0
snake_part = 20
x = 200
y = 280
x_change = y_change = 0
body_snake = []
length = 1

# Create Point
point_x = random.randint(0, 19) * snake_part + 20
point_y = random.randint(0, 19) * snake_part + 80

# Snake speed
clock = pygame.time.Clock()
speed = 3

# Load icon continue
play = pygame.image.load(r'assets\img\play.png')
play = pygame.transform.scale(play, (100, 50))  # Điều chỉnh kích thước icon

# Function check collision
def check_col():
    # Check collision with point return 0:
    if x < 20 or x >= width - 20 or y < 80 or y >= height - 20 or [x, y] in body_snake[:-1]:
        return 2
    return 1

def score_view(score, highScore):
    font = pygame.font.Font(None, 30)
    score = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score, (10, 10))
    highScore = font.render(f"High Score: {highScore}", True, (255, 255, 255))
    window.blit(highScore, (10, 30))


# Main loop
running = True

# gameplay 0: Menu 1 : Game running, 2: Game over , 3: Pause
gameplay = 1

while running:
    for event in pygame.event.get():
        # Quit game when user close the window
        if event.type == pygame.QUIT:
            running = False
        # Check key press
        if event.type == pygame.KEYDOWN:

            # Snake move
            if event.key == pygame.K_UP:
                y_change = -snake_part
                x_change = 0
            if event.key == pygame.K_DOWN:
                y_change = snake_part
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = -snake_part
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = snake_part
                y_change = 0

            # Pause game    
            if event.key == pygame.K_ESCAPE:
                if gameplay == 1:
                    gameplay = 3
                else:
                    gameplay = 1

    # Fill the window with black color
    window.blit(background_image, (0, 0))

    # if game running 
    if gameplay == 1:
        score_view(score, highScore)
        # Update Snake position
        x += x_change
        y += y_change
        # Add snake part
        body_snake.append([x, y])
        # Remove snake part
        if len(body_snake) > length:
            del body_snake[0]
        # Check Snake eat point
        if x == point_x and y == point_y:
            length += 1
            score += 1
            if score > highScore:
                highScore = score
            point_x = random.randint(0, 19) * snake_part + 20
            point_y = random.randint(0, 19) * snake_part + 80

            eat_sound.play()
        # Draw Snake    
        for x, y in body_snake:
            pygame.draw.rect(window, (255, 255, 255), (x, y, snake_part, snake_part))

        # Draw Point
        pygame.draw.rect(window, (255, 0, 0), (point_x, point_y, snake_part, snake_part))

        # Check collision return 2: Game Over
        gameplay = check_col()

        if gameplay == 2:
            over_sound.play(1)

        clock.tick(speed)

    elif gameplay == 2:
        # Game Over
        font = pygame.font.Font(None, 30)
        text = font.render("GAME OVER", True, (255, 255, 255))
        window.blit(text, (width // 2 - 50, height // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(1000)
        # Reset game
        x = 200
        y = 280
        x_change = y_change = 0
        body_snake = []
        length = 1
        score = 0
        point_x = random.randint(0, 19) * snake_part + 20
        point_y = random.randint(0, 18) * snake_part + 80
        running = True


    elif gameplay == 3:
        font = pygame.font.Font(None, 30)
        text = font.render("Pause", True, (255, 255, 255))
        window.blit(text, (width // 2 - 50, height // 2 - 50))

        # Vẽ icon tiếp tục khi game ở trạng thái pause
        icon_rect = play.get_rect(center=(width // 2, height // 2 + 50))
        window.blit(play, icon_rect)

        # Kiểm tra sự kiện nhấn chuột vào icon tiếp tục
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if icon_rect.collidepoint(mouse_x, mouse_y):
                gameplay = 1  # Tiếp tục trò chơi khi nhấn vào icon

    # Cập nhật màn hình
    pygame.display.flip()
# End game loop
# clear memory
pygame.mixer.quit()
# clear screen
window.fill((0, 0, 0))
# Quit Pygame
pygame.quit()
quit()
