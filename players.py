import pygame
import random
import math
import time
from Particle import Particle

background_color = (255, 255, 255)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.deletelist = []
        self.direction = 'up'
        self.snake = Particle(self.x, self.y, 64)
        self.deleter = Particle(self.x, self.y, 64)
        self.snakebody = Particle(self.x-64,self.y-64,64)
        self.snakebody.change_color(0, 255, 0)
        self.deleter.change_color(255, 255, 255)

    def spawn_in(self):
        #print(self.x)
        #print(self.y)
        self.deletelist.append((self.snake.position()))
        #self.deletelist.append((self.snakebody.position()))
        self.deleter.displace(self.deletelist[0])
        self.deleter.display()
        self.deletelist.remove(self.deletelist[0])
        self.snake.movegrid()
        #self.snakebody.movegrid()
        self.snake.display()
        #self.snakebody.display()
        
        
    
    def turn(self, direction):
        self.direction = str(direction)
        self.snake.change_direction(direction) 


    