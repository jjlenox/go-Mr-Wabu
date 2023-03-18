import pygame
import random
import math
import time
from Particle import Particle

background_color = (255, 255, 255)
i = 0

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.deletelist = []
        self.direction = 'up'
        self.snake = Particle(self.x, self.y, 64)
        self.deleter = Particle(self.x, self.y, 64)
        self.snakebody = Particle(self.x,self.y,64)
        self.snakebody.change_color(0, 255, 0)
        self.deleter.change_color(255, 255, 255)
        self.i = 0

    def spawn_in(self):
        if self.i != 60:
            self.i += 1
        #print(self.x)
        #print(self.y)
        self.deletelist.append((self.snake.position()))
        
        self.deleter.displace(self.deletelist[-1])
        self.deleter.display()
        self.deletelist.remove(self.deletelist[-1])
            
        self.snake.movegrid()
        self.snake.display()

        
        
    
    def turn(self, direction):
        self.direction = str(direction)
        self.snake.change_direction(direction) 


    