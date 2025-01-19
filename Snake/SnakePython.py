# Description: Tạo cửa sổ Pygame
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Linhpro')

# Set up icon
icon=pygame.image.load(r'assets\icon.png')
pygame.display.set_icon(icon)

#Variables
snake_part=20
x=y=200
x_change=y_change=0
body_snake=[]
length= 1

# create Point
point_x= random.randint(0,19)*400

# Main loop
running = True
while running:
    for event in pygame.event.get():
        # quit game when user close the window
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black color
    window.fill((0, 0, 0))

    # cập nhật
    pygame.display.flip()

# Quit Pygame
pygame.quit()
quit()