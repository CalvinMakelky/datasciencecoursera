import pygame
from random import randint
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
WIDTH = 640
HEIGHT = 480
lives = 3
cooldown = 60 
frog_path = 'frog.jpg'
truck_path = 'truck.jpg'
done = False
round = 1
clock = pygame.time.Clock()

class Frog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 320 -33
        self.y = 410
        self.speed = 4
        self.image = pygame.image.load('frog.jpg')
        self.rect = pygame.Rect(self.x+28, self.y+28, 91, 66)
class truck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = randint(192, WIDTH-192)
        self.y = randint(0, HEIGHT-150)
        self.dx = round
        self.image = pygame.image.load('truck.jpg')
        self.rect = pygame.Rect(self.x+28, self.y+28, 192, 48)
    def move(self):
        if(self.x<=0):
            self.dx = round
        elif(self.x>=WIDTH-192):
            self.dx = -round
        self.x += self.dx
        self.rect = pygame.Rect(self.x + 28, self.y + 28, 192, 48)
frog = Frog()
truck1 = truck()
truck2 = truck()
truck3 = truck()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if lives == 0:
        frog = Frog()
        truck1 = truck()
        truck2 = truck()
        truck3 = truck()
        round=1
        lives = 3
    if frog.y == 0:
        frog = Frog()
        truck1 = truck()
        truck2 = truck()
        truck3 = truck()
        round+=1
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if(frog.y>0):
            frog.y -= 5
            frog.rect.move(frog.x, frog.y)
            frog.rect = pygame.Rect(frog.x + 28, frog.y + 28, 91, 66)
    if pressed[pygame.K_DOWN]:
        if(frog.y<410):
            frog.y += 5
            frog.rect.move(frog.x, frog.y)
            frog.rect = pygame.Rect(frog.x + 28, frog.y + 28, 91, 66)
    if pressed[pygame.K_LEFT]:
        if(frog.x>0):
            frog.x -= 5
            frog.rect.move(frog.x, frog.y)
            frog.rect = pygame.Rect(frog.x + 28, frog.y + 28, 91, 66)
    if pressed[pygame.K_RIGHT]:
        if(frog.x<548):
            frog.x +=5
            frog.rect.move(frog.x, frog.y)
            frog.rect = pygame.Rect(frog.x + 28, frog.y + 28, 91, 66)                      
         
    screen.fill([0,0,0])

    truck1.move()
    truck2.move()
    truck3.move()

    if(cooldown >= 60):
        if(frog.rect.colliderect(truck1)):
            lives -= 1
            cooldown = 0
            screen.fill([90, 0, 0])
            frog = Frog()
            truck1 = truck()
            truck2 = truck()
            truck3 = truck()
        if(frog.rect.colliderect(truck2)):
            lives -= 1
            cooldown = 0
            screen.fill([90, 0, 0])
            frog = Frog()
            truck1 = truck()
            truck2 = truck()
            truck3 = truck()
        if(frog.rect.colliderect(truck3)):
            lives -= 1
            cooldown = 0
            screen.fill([90, 0, 0])
            frog = Frog()
            truck1 = truck()
            truck2 = truck()
            truck3 = truck()

    font = pygame.font.Font(None, 36)
    text = font.render("Lives: ", 1, (90, 90, 90))
    screen.blit(text, (360,0))
    col = str(lives)
    text2 = font.render(col, 1, (90,90,90))
    screen.blit(text2, (450, 0))
    rd = str(round)
    text3 = font.render("Round: ", 1, (90,90,90))
    screen.blit(text3, (200, 0))
    text4 = font.render(rd, 1, (90,90,90))
    screen.blit(text4, (300, 0))

    screen.blit(frog.image, (frog.x,frog.y))
    screen.blit(truck1.image, (truck1.x, truck1.y))
    screen.blit(truck2.image, (truck2.x, truck2.y))
    screen.blit(truck3.image, (truck3.x, truck3.y))

    if(cooldown < 60):
        cooldown += 1

    pygame.display.flip()
    clock.tick(60)
