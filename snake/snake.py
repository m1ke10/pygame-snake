import pygame
import sys
import tkinter as tk
from tkinter import messagebox
import random
import math
import os
# Create the main application window (optional)
root = tk.Tk()
root.withdraw()  # Hide the main window (it won't be shown)

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
points = 1
xvel = 10
yvel = 0
# Set the color of the square (in RGB format)
square_color = (255, 255, 255)  # Red
clock = pygame.time.Clock()
# Define the square's position and size
square_x = 10  # 10 pixels to the right of the left border
square_y = 10  # 10 pixels below the top border
square_width = 10
square_height = 10
position_x = []
position_y = []
position_apple_x_gross = random.randrange(1, 63)
position_apple_y_gross = random.randrange(1, 47)
pygame.mixer.music.load("youtube_rRnBZWwAIWc_audio.mp3")
pygame.mixer.music.play(-1)
def you_lose(max_score):
    pygame.quit()
    messagebox.showinfo("You lost!", "Max score: " + str(max_score))
    sys.exit()
    pygame.mixer.music.stop()
font = pygame.font.Font(None, 36)  # You can specify the font file and size here (None uses the default font)
# Main game loop
running = True
while running:
    position_apple_x = position_apple_x_gross * 10
    position_apple_y = position_apple_y_gross * 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xvel = -10
        yvel = 0
        
    if keys[pygame.K_RIGHT]:
        xvel = 10
        yvel = 0
    if keys[pygame.K_UP]:
        xvel = 0
        yvel = -10
    if keys[pygame.K_DOWN]:
        xvel = 0
        yvel = 10
    if square_x > 630:
        xvel = 0
        yvel = 0
        square_x = 630
        you_lose(points)
    if square_x < 1:
        square_x = 0
        xvel = 0
        yvel = 0
        you_lose(points)
    if square_y > 470:
        xvel = 0
        yvel = 0
        square_x = 470
        you_lose(points)
    if square_y < 1:
        square_y = 0
        xvel = 0
        yvel = 0
        you_lose(points)
    def are_last_elements_duplicated():
        if not position_x or not position_y:
            return False 
        last_x = position_x[-1]
        last_y = position_y[-1]
    
        for x, y in zip(position_x[:-1], position_y[:-1]):
            if x == last_x and y == last_y:
                return True  # Duplicates found in both lists
        return False  # No duplicates found
    if are_last_elements_duplicated():
        you_lose(points)
    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black to clear the previous frame
    square_x += xvel
    square_y += yvel
    # Draw the square
    if not len(position_x) - 1 > points:
        position_x.append(square_x)
        position_y.append(square_y)
    if len(position_x) - 1 == points:
         position_x.remove(position_x[0])
         position_y.remove(position_y[0])
    # Update the display
    for x, y in zip(position_x, position_y):
        pygame.draw.rect(screen, square_color, (x, y, square_width, square_height))
    if position_x[-1] == position_apple_x and position_y[-1] == position_apple_y:
        points += 1
        position_apple_x_gross = random.randrange(1, 63)
        position_apple_y_gross = random.randrange(1, 47)
    pygame.draw.rect(screen, (255, 0, 0), (position_apple_x, position_apple_y, square_width, square_height))
    text = "Score: " + str(points - 1)  # Your text here
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (50, 18)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(12)
# Quit Pygame
pygame.quit()
sys.exit()
