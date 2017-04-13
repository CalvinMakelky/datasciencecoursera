'''
import pygame
 
pygame.init()

SIZE= width,height = 640, 480

window = pygame.display.set_mode(SIZE)
display_surface =pygame.display.get_surface()
display_rectange=display_surface.get_rect()
 
pygame.display.set_caption("Collision Detection")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
green = (25, 150, 150)

direction ='right'

moveX,moveY=0,0

SPEED = [2,0]

ghostx=8
ghosty=8
x=0
y=0
hits=0

clock = pygame.time.Clock()



def text(hits):
    font=pygame.font.SysFont("monospace",15)
    hitLabel=font.render("Hits: " + str(hits),1,(black))
    window.blit(hitLabel, (300,10))

def detectCollisions(Sprite1, badGuy):
     if Sprite1.rect.colliderect(sprite2.rect) == True:
         return True
     elif Sprite1.rect.colliderect(sprite3.rect) == True:
         return True
     elif Sprite1.rect.colliderect(sprite4.rect) == True:
         return True
def Scoring(Sprite1, badGuy):
    if badguy.colliding==False and detectCollisions(Sprite,badGuy)==True:
        hits+=1
        badguy.colliding=True
    elif not detectCollisions(Sprite1.badguy)==True:
        badGuy.colliding=False
'''
'''       

class Pacman(pygame.sprite.Sprite):

    def __init__(self,x,y,image="pacman.png",speed=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.speed=speed
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y=300

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class Ghost(pygame.sprite.Sprite):

    colliding = False
    def __init__(self,image="ghost.png",speed=[4,0]):
        pygame.sprite.Sprite.__init__(self)
        self.speed=speed
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()

    def update(self):
        global SIZE
        if (self.rect.x <0) or (self.rect.x > 640-110):
            self.speed[0] *= -1
        if (self.rect.y<0) or (self.rect.y > 480-110):
            self.speed[1] *= -1

        self.rect.x =self.rect.x + self.speed[0]
        self.rect.y =self.rect.y + self.speed[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def render(self,collision):
        if (collision==True):
            global hits
            pygame.draw.rect(window,red,(self.x,self.y,self.width,self.height))
            hits+=1
        else:
            pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))
ghost = Ghost()
ghost2 = Ghost()
ghost3 = Ghost()
pacman = Pacman()

pacman.x+=moveX
pacman.y+=moveY
 

 
gameLoop=True
while gameLoop:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                moveX = -8
            if (event.key==pygame.K_RIGHT):
                moveX = 8
            if (event.key==pygame.K_UP):
                moveY = -8
            if (event.key==pygame.K_DOWN):
                moveY = 8
        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_LEFT):
                moveX=0
            if (event.key==pygame.K_RIGHT):
                moveX=0
            if (event.key==pygame.K_UP):
                moveY=0
            if (event.key==pygame.K_DOWN):
                moveY=0
    
                
    window.fill(green)

    text(hits)

    ghost.draw(window)
    ghost.update()

    pacman.draw(window)
    
 
    pygame.display.flip()
 
    clock.tick(50)
 
pygame.quit()
'''

import pygame
 
pygame.init()

SIZE=width,height =640, 480

window = pygame.display.set_mode(SIZE)
display_surface =pygame.display.get_surface()
display_rectange=display_surface.get_rect()
 
pygame.display.set_caption("Collision Detection")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)
green = (25, 150, 150)

direction ='right'

hits=0

clock = pygame.time.Clock()

ghost_img = pygame.image.load("ghost.png")
ghost = ghost_img.convert_alpha()



def text(hits):
    font=pygame.font.SysFont("monospace",15)
    hitLabel=font.render("Hits: " + str(hits),1,(black))
    window.blit(hitLabel, (300,10))
    
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2,x3,y3,w3,h3,x4,y4,w4,h4):
 
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
        return True
    elif (x3+w3>=x1>=x3 and y3+h3>=y1>=y3):
        return True
    elif (x3+w3>=x1+w1>=x3 and y3+h3>=y1>=y3):
        return True
    elif (x3+w3>=x1>=x3 and y3+h3>=y1+h1>=y3):
        return True
    elif (x3+w3>=x1+w1>=x3 and y3+h3>=y1+h1>=y3):
        return True
    elif (x4+w4>=x1>=x4 and y4+h4>=y1>=y4):
        return True
    elif (x4+w4>=x1+w1>=x4 and y4+h4>=y1>=y4):
        return True
    elif (x4+w4>=x1>=x4 and y4+h4>=y1+h1>=y4):
        return True
    elif (x4+w4>=x1+w1>=x4 and y4+h4>=y1+h1>=y4):
        return True
    else:
        return False


class Sprite:
    colliding = False
    def __init__(self,x,y,width,height,image='ghost.png'):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
    
    def render(self,collision):
            if (collision==True):
                global hits
                pygame.draw.rect(window,red,(self.x,self.y,self.width,self.height))
                hits+=1
            else:
                pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))
                pygame.Surface.blit(ghost, window,(self.x,self.y,self.width,self.height))
                

Sprite1=Sprite(50,400,50,50)
Sprite2=Sprite(200,350,50,50)
Sprite3=Sprite(300,120,50,50)
Sprite4=Sprite(500,200,50,50)
 
moveX,moveY=0,0

ghostx=8
ghost2x=4
ghost3x=4


gameLoop=True
while gameLoop:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                moveX = -8
            if (event.key==pygame.K_RIGHT):
                moveX = 8
            if (event.key==pygame.K_UP):
                moveY = -8
            if (event.key==pygame.K_DOWN):
                moveY = 8
        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_LEFT):
                moveX=0
            if (event.key==pygame.K_RIGHT):
                moveX=0
            if (event.key==pygame.K_UP):
                moveY=0
            if (event.key==pygame.K_DOWN):
                moveY=0
                
    window.fill(green)

    text(hits)
    
    Sprite1.x+=moveX
 
    Sprite1.y+=moveY

    Sprite2.x+=ghostx

    Sprite3.x+=ghost2x

    Sprite4.x+=ghost3x
    
    if Sprite2.x == 592:
        ghostx*= -1
    elif Sprite2.x == 0:
        ghostx*= -1
    if Sprite3.x == 592:
        ghost2x*= -1
    elif Sprite3.x == 0:
        ghost2x*= -1
    if Sprite4.x == 592:
        ghost3x*= -1
    elif Sprite4.x == 0:
        ghost3x*= -1
    
    
    collisions=detectCollisions(Sprite1.x,Sprite1.y,Sprite1.width,Sprite1.height,
                                Sprite2.x,Sprite2.y,Sprite2.width,Sprite2.height,
                                Sprite3.x,Sprite3.y,Sprite3.width,Sprite3.height,
                                Sprite4.x,Sprite4.y,Sprite4.width,Sprite4.height,)
    
    Sprite1.render(collisions)
 
    Sprite2.render(False)
    Sprite3.render(False)
    Sprite4.render(False)
 
    pygame.display.flip()
 
    clock.tick(50)
 
pygame.quit()
