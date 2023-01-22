import pygame
from datetime import datetime

# Initialize pygame
pygame.init()

# Set the window size and title
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fantasy Console")

# Create a button for the start menu
start_button = pygame.Rect(10, 10, 50, 30)

# Create a font for the taskbar
font = pygame.font.Font(None, 20)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                # Open the start menu when the button is clicked
                pass
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the taskbar
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 800, 50))

    # Draw the start button
    pygame.draw.rect(screen, (255, 0, 0), start_button)

    # Get the current time and date
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m/%d/%Y")

    # Render the time and date as text
    time_text = font.render(current_time, True, (0, 0, 0))
    date_text = font.render(current_date, True, (0, 0, 0))

    # Draw the time and date on the taskbar
    screen.blit(time_text, (700, 10))
    screen.blit(date_text, (600, 10))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
