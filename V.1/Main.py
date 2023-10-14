import pygame
import random as rd
from math import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
size = (800, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False

fps = 60
 
clock = pygame.time.Clock()
v_max = 10e-5

position_x = rd.randint(300,500)
position_y = rd.randint(300,500)
velocity_x = rd.random()*v_max-v_max/2
velocity_y = rd.random()*v_max-v_max/2
mass = rd.randint(10e7,10e10)
volumic_mass = 5.515e6

mouse_mass = mass

G = 6.674e-11
g = 9.81

resitance = 1 # facteur de perte par seconde 

entity = [position_x, position_y, velocity_x, velocity_y, mass, volumic_mass]

xyz = True
 
# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        mouse_mass += mouse_mass*2/fps
    if keys[pygame.K_DOWN]:
        mouse_mass -= mouse_mass*2/fps
    if keys[pygame.K_RIGHT]:
        resitance += resitance*2/fps
    if keys[pygame.K_LEFT]:
        resitance -= resitance*2/fps

    x, y = pygame.mouse.get_pos()

    dist_planet_other_planet = sqrt((x-position_x)**2  +  (y-position_y)**2) # distance entre 2 planetes
    a = G  * ( (mouse_mass*mass)  /  dist_planet_other_planet)  /  mass # calcule Force de gravitation

    velocity_x = (x-position_x)*a + velocity_x*(1-resitance/fps) # calcule acceleration en x
    velocity_y = (y-position_y)*a + velocity_y*(1-resitance/fps) # calcule acceleration en y

    position_x += velocity_x
    position_y += velocity_y

    screen.fill(WHITE)

    font = pygame.font.SysFont("comicsansms", 36)
    text_surface = font.render(str(mouse_mass), True, (0, 128, 0))

    screen.blit(text_surface, (0,0))

    pygame.draw.line(screen, GREEN,(position_x,position_y), (x,y))
    pygame.draw.circle(screen,RED,(position_x,position_y),10)
 
    pygame.display.flip()
 
    clock.tick(fps)
 
pygame.quit()