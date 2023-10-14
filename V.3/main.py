import pygame
import random as rd
from math import *
import time
from interface import *

pygame.init()

# --------- val main ---------

size = (1200, 700)
fps = 120

# --------- val ball ---------

position_x = 400 # position en px
position_y = 400
velocity_x = 0 # velocity en m/s
velocity_y = 0
m_px = 100 # 1m est equivalent a 100px
mass = 1000 # en kg
g = 9.81 # en m/s**2
resitance = 1 # facteur de perte par seconde en %
elasticity = 1000 * m_px # facteur d'élasticité en kg/m/s
taille = 1 * m_px # la taille normal de l'élastique en m
taille_max = 5 * m_px# la taille maximal avant qui l'elastique casse en m
elastique_type = ("extension", "tout")[0] #choisir le type d'élastique

# --------- val color ---------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# --------- pygame init ---------

clock = pygame.time.Clock()
font = pygame.font.Font("Project_Elastique/V.3/font/Arcade.ttf", 35)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
text_surface_1 = font.render("gravite : " + str(round(g, 3)) + "m/s" , True, (0, 128, 0))
text_surface_2 = font.render("perte v/s : " + str(round(resitance, 3)) + "%", True, (0, 128, 0))

# --------- val other ---------

done = False
nb_points = 0
points = [(0,0)]
t_push = 0.5
t_start = time.time()
t_stop = time.time()
t_fps = clock.get_fps()
pause = False
 
# -------- Main Program Loop -----------

Interface(screen)
position_x, position_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]+taille

while not done:

    screen.fill(WHITE)

    keys = pygame.key.get_pressed()
    points[0] = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if keys[pygame.K_UP]:
        g += g*2/fps
        text_surface_1 = font.render("gravite : " + str(round(g, 3)) + "m/s" , True, (0, 128, 0))
    if keys[pygame.K_DOWN]:
        g -= g*2/fps
        text_surface_1 = font.render("gravite : " + str(round(g, 3)) + "m/s" , True, (0, 128, 0))
    if keys[pygame.K_RIGHT]:
        resitance += resitance*2/fps
        text_surface_2 = font.render("perte v/s : " + str(round(resitance, 3)) + "%", True, (0, 128, 0))
    if keys[pygame.K_LEFT]:
        resitance -= resitance*2/fps
        text_surface_2 = font.render("perte v/s : " + str(round(resitance, 3)) + "%", True, (0, 128, 0))
    if keys[pygame.K_n] and t_stop - t_start > t_push:
        points.append(points[0])
        t_start = time.time()
    if keys[pygame.K_p] and t_stop - t_start > t_push:
        pause = False if pause else True
        print(pause)
    if keys[pygame.K_ESCAPE]:
        Interface(screen)

    for point in points:

        x, y = point

        distance = sqrt((x-position_x)**2 + (y-position_y)**2)
        print((distance-taille)/m_px)

        if not pause:

            if distance > taille and elastique_type == "extension":

                velocity_x += (x-position_x)*elasticity*(1-taille/distance)/(fps*m_px*mass)
                velocity_y += (y-position_y)*elasticity*(1-taille/distance)/(fps*m_px*mass)

                tension = ((distance-taille))/(taille_max) 

            if elastique_type == "tout":


                velocity_x += (x-position_x)*elasticity*(1-taille/distance)/(fps*m_px*mass)
                velocity_y += (y-position_y)*elasticity*(1-taille/distance)/(fps*m_px*mass)

                tension = 0
    

        COLOR = [255-255/(1+tension),255/(1+tension),0]

        pygame.draw.line(screen, COLOR,(position_x,position_y), (x,y))

    if not pause:

        velocity_x = velocity_x*(1-resitance/fps)
        velocity_y = g/fps*m_px + velocity_y*(1-resitance/fps)

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