import pygame
import random
import math
import time
from Particle import Particle


class Edibles:
    def __init__(self):
        self.x = 32
        self.y = 32
        self.deletelist = []
        self.edible = Particle(self.x*random.randint(1,10), self.y*random.randint(1,10), 64)

    def spawn_in(self):
        self.edible.display()
