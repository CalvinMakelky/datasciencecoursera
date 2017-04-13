import pygame, sys
from pygame.locals import *
'''
pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('ghost.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 325:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
'''
'''
import sys, pygame
pygame.init()
speed_x = 1
speed_y = 0

black = (0, 0, 0)
width, height = 320, 240
size = ( width, height )

screen = pygame.display.set_mode(size)
display_surface = pygame.display.get_surface()
display_rectangle = display_surface.get_rect()

ball_img = pygame.image.load("ghost.png")
ball = ball_img.convert_alpha()
ballrect = ball.get_rect()

while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if not display_rectangle.contains( ballrect.move([speed_x, 0]) ):
            speed_x *= -1
        else:
            ballrect = ballrect.move([speed_x, 0])

        if not display_rectangle.contains( ballrect.move([0, speed_y]) ):
            speed_y *= -1
        else:
            ballrect = ballrect.move([0, speed_y])  

        screen.fill(black)
        screen.blit(ball, ballrect)
        screen.blit(ball, ballrect)
        pygame.display.flip()
        pygame.time.delay(30)
'''
import sys, pygame, random

SIZE = width, height = 640, 480
SPEED = [1, 0]
black = 0, 0, 0

class mySprite(pygame.sprite.Sprite):
    def __init__(self, image="ghost.png", speed=[1,0]):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def update(self):
        global SIZE
        #i used 110 px because it's the size of the image, but it's better to use the rect property of the pygame
        if (self.rect.x <0) or (self.rect.x > 640-110):
            self.speed[0] *= -1
        if (self.rect.y<0) or (self.rect.y > 480-110):
            self.speed[1] *= -1

        self.rect.x =self.rect.x + self.speed[0]
        self.rect.y =self.rect.y + self.speed[1]

#OR:        self.rect = self.rect.move(self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


#    
pygame.init()
screen = pygame.display.set_mode(SIZE)

ghost = mySprite()
ghost2 = mySprite()
ghost3= mySprite()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    ghost.draw(screen)
    ghost.update()
    '''
    ghost2.draw(screen,(100,100))
    ghost2.update()
    ghost3.draw(screen)
    ghost3.update()
    '''
    pygame.display.flip()











