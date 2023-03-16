import pygame
import random
import math
import time

(width, height) = (1920, 1080)
background_color = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Go Mr. Wamu')
screen.fill(background_color)

class Particle:

    def __init__(self, x, y, size):
        self.empty = True
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 1
        self.speed = 1
        self.angle = math.pi/3
        self.ticks = 200
        self.direction = 'up'
    def display(self):
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)
    def change_direction(self, string):
        self.direction = string
    def slide(self, frame):
        
        if self.direction == 'up':
            for n in range(frame):
                rect = pygame.Rect(self.x, self.y+20-n, self.size, self.size)
                pygame.draw.rect(screen, self.color, rect)
                if self.color == (0, 100, 0):
                    screen.blit(image, (self.x, self.y+20-n))
                
                pygame.display.flip()
                pygame.time.Clock().tick(self.ticks)
        elif self.direction == 'down':
            for n in range(frame):
                pygame.draw.circle(screen, self.color, (self.x, self.y+20/(n+1)), self.size)
                pygame.display.flip()
                pygame.time.Clock().tick(self.ticks)
        elif self.direction == 'left':
            for n in range(frame):
                pygame.draw.circle(screen, self.color, (self.x-20/(frame-(n)), self.y), self.size)
                pygame.display.flip()
                pygame.time.Clock().tick(self.ticks)   
        elif self.direction == 'right':
            for n in range(frame):
                pygame.draw.circle(screen, self.color, (self.x+20/(n+1), self.y), self.size)
                pygame.display.flip()
                pygame.time.Clock().tick(self.ticks)
    
    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
    def new_speed(self, speed):
        self.speed = speed
    def bounce(self):
        if self.x >= width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
        elif self.x <= self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
        if self.y >= height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y <= self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
    
    def green(self):
        self.color = (0, 200, 0)
    def greenHead(self):
        self.color = (0, 100, 0)

    def yellow(self):
        self.color = (252, 177, 3)
    def yellowHead(self):
        self.color = (43, 32, 5)

    def clear(self):
        self.color = (0, 0, 255)
    def get_color(self):
        return self.color




def findParticle(particles, x, y):
        for p in particles:
            if math.hypot(p.x-x, p.y-y) <= p.size:
                return p
        return None
def findParticleposition(particles, x, y):
        position = 0
        for p in particles:
            if math.hypot(p.x-x, p.y-y) <= p.size:
                return position
            position += 1
        return None

rows, cols = (25,16) #28
particle_list = []
grid = [[0 for i in range(cols)] for j in range(rows)]
screen.fill(background_color)
for i in range(rows):
   for j in range(cols):
        particle = Particle(64*i+32, 64*j+32, 64)
        grid[i][j] = len(particle_list)
        particle_list.append(particle)
        particle.display()
running = True
#center
apple_list = []
i = 6
j = 6
snake_head = particle_list[grid[i][j]]
snake_head.display()
delete_list = []
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
direction =  UP

i2 = 5
j2 = 5
snake_head2 = particle_list[grid[i][j]]
snake_head2.display()
delete_list2 = []
direction2 =  UP

image = pygame.image.load("head.png").convert_alpha()

apple_ticks = 0
clock = pygame.time.Clock()
while running:
    appleEaten = False




    for n in apple_list:
        particle_list[n].display()
#up
    if (j > 0) and direction == 'up':
        current_position = grid[i][j]
        delete_list.append(current_position)
        j -= 1
        for n in apple_list:
            if particle_list[grid[i][j]].get_color() == (255,0,0):
                appleEaten = True
        snake_head = particle_list[grid[i][j]]
        snake_head.greenHead()
        snake_head.change_direction(UP)
        snake_head.display()
        if appleEaten == False:
            particle_list[delete_list[0]].color = (0, 0, 255)
            particle_list[delete_list[0]].change_direction(UP)
            particle_list[delete_list[0]].display()
            delete_list.remove(delete_list[0])
#down  
    elif (j < cols-1) and direction == 'down':
        current_position = grid[i][j]
        delete_list.append(current_position)
        j += 1
        for n in apple_list:
            if particle_list[grid[i][j]].get_color() == (255,0,0):
                appleEaten = True
        snake_head = particle_list[grid[i][j]]
        snake_head.greenHead()
        snake_head.change_direction(DOWN)
        snake_head.display()
        if appleEaten == False:
            particle_list[delete_list[0]].color = (0, 0, 255)
            particle_list[delete_list[0]].change_direction(DOWN)
            particle_list[delete_list[0]].display()
            delete_list.remove(delete_list[0])
#left        
    elif (i > 0) and direction == 'left':
        current_position = grid[i][j]
        delete_list.append(current_position)
        i -= 1
        for n in apple_list:
            if particle_list[grid[i][j]].get_color() == (255,0,0):
                appleEaten = True
        snake_head = particle_list[grid[i][j]]
        snake_head.greenHead()
        snake_head.change_direction(LEFT)
        snake_head.display()
        if appleEaten == False:
            particle_list[delete_list[0]].color = (0, 0, 255)
            particle_list[delete_list[0]].change_direction(LEFT)
            particle_list[delete_list[0]].display()
            delete_list.remove(delete_list[0])
#right        
    elif (i < rows-1) and direction == 'right':
        current_position = grid[i][j]
        delete_list.append(current_position)
        i += 1
        for n in apple_list:
            if particle_list[grid[i][j]].get_color() == (255,0,0):
                appleEaten = True
        snake_head = particle_list[grid[i][j]]
        snake_head.greenHead()
        snake_head.change_direction(RIGHT)
        snake_head.display()
        if appleEaten == False:
            particle_list[delete_list[0]].color = (0, 0, 255)
            particle_list[delete_list[0]].change_direction(RIGHT)
            particle_list[delete_list[0]].display()
            delete_list.remove(delete_list[0])
    else:
        print('gamelost')
        running = False
    for n in delete_list:
        particle_list[n].green()
        particle_list[n].display()
    snake_head.greenHead()
    snake_head.display()
    """
#player 2
    
    appleEaten = False

    if (j2 > 0) and direction2 == 'up':
        current_position2 = grid[i2][j2]
        delete_list2.append(current_position2)
        j2 -= 1
        for n in apple_list:
            if particle_list[grid[i2][j2]].get_color() == (255,0,0):
                appleEaten = True
        snake_head2 = particle_list[grid[i2][j2]]
        snake_head2.yellowHead()
        snake_head2.display()
        if appleEaten == False:
            particle_list[delete_list2[0]].color = (0, 0, 255)
            particle_list[delete_list2[0]].display()
            delete_list2.remove(delete_list2[0])
#down  
    elif (j2 < cols-1) and direction2 == 'down':
        current_position2 = grid[i2][j2]
        delete_list2.append(current_position2)
        j2 += 1
        for n in apple_list:
            if particle_list[grid[i2][j2]].get_color() == (255,0,0):
                appleEaten = True
        snake_head2 = particle_list[grid[i2][j2]]
        snake_head2.yellowHead()
        snake_head2.display()
        if appleEaten == False:
            particle_list[delete_list2[0]].color = (0, 0, 255)
            particle_list[delete_list2[0]].display()
            delete_list2.remove(delete_list2[0])
#left        
    elif (i2 > 0) and direction2 == 'left':
        current_position2 = grid[i2][j2]
        delete_list2.append(current_position2)
        i2 -= 1
        for n in apple_list:
            if particle_list[grid[i2][j2]].get_color() == (255,0,0):
                appleEaten = True
        snake_head2 = particle_list[grid[i2][j2]]
        snake_head2.yellowHead()
        snake_head2.display()
        if appleEaten == False:
            particle_list[delete_list2[0]].color = (0, 0, 255)
            particle_list[delete_list2[0]].display()
            delete_list2.remove(delete_list2[0])
#right        
    elif (i2 < rows-1) and direction2 == 'right':
        current_position2 = grid[i2][j2]
        delete_list2.append(current_position2)
        i2 += 1
        for n in apple_list:
            if particle_list[grid[i2][j2]].get_color() == (255,0,0):
                appleEaten = True
        snake_head2 = particle_list[grid[i2][j2]]
        snake_head2.yellowHead()
        snake_head2.display()
        if appleEaten == False:
            particle_list[delete_list2[0]].color = (0, 0, 255)
            particle_list[delete_list2[0]].display()
            delete_list2.remove(delete_list2[0])
    else:
        print('gamelost')
        running = False
    for n in delete_list2:
        particle_list[n].yellow()
        particle_list[n].display()
    snake_head2.yellowHead()
    snake_head2.display()
    """    
#apples
    apple_ticks += 1
    if apple_ticks > 3:
        position = findParticleposition(particle_list, 20*random.randint(1,rows-1)+10, 20*random.randint(1,cols-1)+10)
        apple_list.append(position)
        particle_list[position].color = (255,0,0)
        particle_list[position].display()
        apple_ticks = 0




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and j > 0:
                direction = UP
            elif event.key == pygame.K_s and j < cols-1:
                direction = DOWN
            elif event.key == pygame.K_a and i > 0:
                direction = LEFT
            elif event.key == pygame.K_d and i < rows-1:
                direction = RIGHT
            #player 2
            if event.key == pygame.K_UP and j2 > 0:
                direction2 = UP
            elif event.key == pygame.K_DOWN and j2 < cols-1:
                direction2 = DOWN
            elif event.key == pygame.K_LEFT and i2 > 0:
                direction2 = LEFT
            elif event.key == pygame.K_RIGHT and i2 < rows-1:
                direction2 = RIGHT

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            position = findParticleposition(particle_list, mouseX, mouseY)
            apple_list.append(position)
            particle_list[position].color = (255,0,0)
            particle_list[position].display()
    
    

    pygame.display.flip()
    clock.tick(4)
    #time.sleep(100000) 


#screen.fill(background_color)
      
