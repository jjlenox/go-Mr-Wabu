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
        self.deleter.change_color(255, 255, 255)

    def spawn_in(self):
        
        self.deletelist.append((self.snake.position()))
        
        self.deleter.displace(self.deletelist[0])
        self.deleter.display()
        self.deletelist.remove(self.deletelist[0])
        self.snake.movegrid()
        self.snake.display()
        
        
        
    
    def turn(self, direction):
        self.direction = str(direction)
        self.snake.change_direction(direction) 


    