import pygame
import random
import math
import time

(width, height) = (1920, 1080)
background_color = (255, 255, 255)
UP = 0
DOWN = math.pi
LEFT = 3*math.pi/2
RIGHT = math.pi/2


screen = pygame.display.set_mode((width, height))

class Particle:

    def __init__(self, x, y, size):
        self.empty = True
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.speed = 2
        self.angle = LEFT
        self.NoDoubleClick = LEFT
        self.previous_angle = UP
        self.completed_path = False
        

    def display(self):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.line(screen, (0,120,0), (self.x, self.y), (self.x+2, self.y+2), 5)

    def change_direction(self, string):
        
        if string == 'up':
            NoDoubleClick = UP
        elif string == 'down':
            NoDoubleClick = DOWN
        elif string == 'left':
            NoDoubleClick = LEFT
        elif string == 'right':
            NoDoubleClick = RIGHT
        if self.completed_path == True:
            if self.previous_angle != self.angle and self.angle != NoDoubleClick:
                self.previous_angle = self.angle
            if string == 'up':
                self.angle = UP
            elif string == 'down':
                self.angle = DOWN
            elif string == 'left':
                self.angle = LEFT
            elif string == 'right':
                self.angle = RIGHT

    def displace(self, xy):
        (self.x, self.y) = xy

                
    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def movegrid(self):
        print('x: ' + str(self.x))
        print('y: ' + str(self.y))
        #up and down
        if (self.angle == UP or self.angle == DOWN) and self.x % 64 == 0:
            self.completed_path = True
            self.y -= math.cos(self.angle) * self.speed
            if self.previous_angle == LEFT:
                    self.x -= self.x % 64
            elif self.previous_angle == RIGHT:
                if self.x % 64 != 0:
                    self.x += 64 - self.x % 64
            else:
                self.y -= math.cos(self.angle) * self.speed
        else:
            #self.completed_path = False #lose control
            self.x += math.sin(self.previous_angle) * self.speed
        #left and right
        if (self.angle == LEFT or self.angle == RIGHT) and self.y % 64 == 0:
            self.completed_path = True
            self.x += math.sin(self.angle) * self.speed
            if self.previous_angle == UP:
                    self.y -= self.y % 64
            elif self.previous_angle == DOWN:
                if self.y % 64 != 0:
                    self.y += 64 - self.y % 64
            else:
                self.x += math.sin(self.angle) * self.speed 
        else:
            #self.completed_path = False
            self.y -= math.cos(self.previous_angle) * self.speed
                        

    
    def position(self):
        return (self.x, self.y )



    def change_speed(self, speed):
        self.speed = speed
    
    def change_color(self, x, y, z):
        self.color = (x, y, z)

    def get_color(self):
        return self.color