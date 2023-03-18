import pygame
import random
import math
import time
from Particle import Particle
from players import Player
from Edibles import Edibles

(width, height) = (1920, 1080)
background_color = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Go Mr. Wamu')
screen.fill(background_color)

#test
running = True
#center
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
direction =  UP


image = pygame.image.load("head.png").convert_alpha()

apple_ticks = 0
clock = pygame.time.Clock()
Player1 = Player(320, 320)
#Player2 = Player(384, 384)
i = False 
while running:
    #grid
    for i in range(width//64):
        pygame.draw.line(screen, (0,0,0), (i*64,0), (i*64,height), 2)
    for j in range(height//64+1):
        pygame.draw.line(screen, (0,0,0), (0,j*64), (width,j*64), 2)
    appleEaten = False


    Player1.spawn_in()
    #Player2.spawn_in()


    #print("hello")

    pygame.display.flip()
    


    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Player1.turn(UP)
            elif event.key == pygame.K_s:
                Player1.turn(DOWN)
            elif event.key == pygame.K_a:
                Player1.turn(LEFT)
            elif event.key == pygame.K_d:
                Player1.turn(RIGHT)
            '''    
            if event.key == pygame.K_i:
                Player2.turn(UP)
            elif event.key == pygame.K_k:
                Player2.turn(DOWN)
            elif event.key == pygame.K_j:
                Player2.turn(LEFT)
            elif event.key == pygame.K_l:
                Player2.turn(RIGHT)
            '''
            #player 2
            """
            if event.key == pygame.K_UP and j2 > 0:
                direction2 = UP
            elif event.key == pygame.K_DOWN and j2 < cols-1:
                direction2 = DOWN
            elif event.key == pygame.K_LEFT and i2 > 0:
                direction2 = LEFT
            elif event.key == pygame.K_RIGHT and i2 < rows-1:
                direction2 = RIGHT
            
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = findParticleposition(particle_list, mouseX, mouseY)
            apple_list.append(position)
            particle_list[position].color = (255,0,0)
            particle_list[position].display()
        """
    

    
    clock.tick(60)
    #time.sleep(100000) 


#screen.fill(background_color)
      
