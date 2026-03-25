import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zad 2")

def draw_rotated_rect(surf, color, center, length, width, angle):
    angle_rad = math.radians(angle)

    # Obliczanie kierunków dla długości i szerokości
    dir_x = math.cos(angle_rad)
    dir_y = math.sin(angle_rad)
    perp_x = -dir_y
    perp_y = dir_x

    # Wyliczanie wierzchołków
    points = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            px = center[0] + i * (length / 2) * dir_x + j * (width / 2) * perp_x
            py = center[1] + i * (length / 2) * dir_y + j * (width / 2) * perp_y
            points.append((px, py))

    ordered_points = [points[0], points[1], points[3], points[2]]
    pygame.draw.polygon(surf, color, ordered_points)

CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    win.fill(BIALY)
    
    pygame.draw.rect(win, CZERWONY, (100, 100, 400, 10))
    pygame.draw.rect(win, CZERWONY, (100, 500, 400, 10))

    draw_rotated_rect(win, CZERWONY, [300, 305], 550, 10, -45)
    
    pygame.display.update()

pygame.quit()