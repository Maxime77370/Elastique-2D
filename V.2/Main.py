import pygame
import random as rd
from math import *
import time
 
pygame.init()

# --------- val main ---------

size = (800, 800)
fps = 60

# --------- val ball ---------

position_x = 400 # position en m/px
position_y = 400
velocity_x = 0 # velocity en m/s
velocity_y = 0
mass = 10 # en kg
g = 9.81 # en m/s
resitance = 1 # facteur de perte par seconde

# --------- val color ---------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# --------- pygame init ---------

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
text_surface_1 = font.render("gravité : " + str(round(g, 3)) + "m/s" , True, (0, 128, 0))
text_surface_2 = font.render("perte v/s : " + str(round(resitance, 3)) + "%", True, (0, 128, 0))

# --------- val other ---------

done = False
nb_points = 0
points = [(0,0)]
t_push = 0.2
t_start = time.time()
t_stop = time.time()
t_fps = clock.get_fps()
 
# -------- Main Program Loop -----------
while not done:

    screen.fill(WHITE)

    keys = pygame.key.get_pressed()
    points[0] = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if keys[pygame.K_UP]:
        g += g*2/fps
        text_surface_1 = font.render("gravité : " + str(round(g, 3)) + "m/s" , True, (0, 128, 0))
    if keys[pygame.K_DOWN]:
        g -= g*2/fps
        text_surface_1 = font.render("gravité : " + str(round(g, 3)) + "m/s" , True, (0, 128, 0))
    if keys[pygame.K_RIGHT]:
        resitance += resitance*2/fps
        text_surface_2 = font.render("perte v/s : " + str(round(resitance, 3)) + "%", True, (0, 128, 0))
    if keys[pygame.K_LEFT]:
        resitance -= resitance*2/fps
        text_surface_2 = font.render("perte v/s : " + str(round(resitance, 3)) + "%", True, (0, 128, 0))
    if keys[pygame.K_n] and t_stop - t_start > t_push:
        points.append(points[0])
        t_start = time.time()

    for point in points:

        x, y = point

        velocity_x += (x-position_x)/fps
        velocity_y += g/fps*10 + (y-position_y)/fps

        tension = sqrt((x-position_x)**2 + (y-position_y)**2)

        COLOR = [255-255/tension,255/tension%255,0]
        print(COLOR)

        pygame.draw.line(screen, COLOR,(position_x,position_y), (x,y))

    velocity_x = velocity_x*(1-resitance/fps)
    velocity_y = velocity_y*(1-resitance/fps)

    position_x += velocity_x
    position_y += velocity_y

    text_surface_3 = font.render( str(round(t_fps, 3)) + " FPS", True, (0, 128, 0))

    screen.blit(text_surface_1, (0,0))
    screen.blit(text_surface_2, (0,20))
    screen.blit(text_surface_3, (size[0]-text_surface_3.get_width(), 0))

    pygame.draw.circle(screen,RED,(position_x,position_y),10)
 
    pygame.display.flip()
 
    clock.tick(fps)
    t_fps = round(clock.get_fps(),1)
    print(t_fps)

    t_stop = time.time()
 
pygame.quit()