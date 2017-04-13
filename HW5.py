import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
collisions = 0
cooldown = 60 #invulnerability frames!
cat_path = 'cat.png'
scary_path = 'scary.png'
done = False

clock = pygame.time.Clock()

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 512
        self.y = 359
        self.speed = 5
        self.image = pygame.image.load('cat.png')
        self.rect = pygame.Rect(self.x + 28, self.y + 28, 100, 100)

class Scary(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.dx = 5
        self.image = pygame.image.load('scary.png')
        self.rect = pygame.Rect(self.x + 28, self.y + 28, 100, 100)

    def move(self):
        if(self.x<=0):
            self.dx = 5
        elif(self.x>=512):
            self.dx = -5

        self.x += self.dx
        self.rect = pygame.Rect(self.x + 28, self.y + 28, 100, 100)

cat = Cat()
scary1 = Scary()
scary2 = Scary()
scary3 = Scary()

scary2.y = 160
scary2.x = 512
scary3.y = (160+160)
scary3.x = 50


while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if(cat.y>0):
            cat.y -= 5
            cat.rect.move(cat.x, cat.y)
            cat.rect = pygame.Rect(cat.x + 28, cat.y + 28, 100, 100)
    if pressed[pygame.K_DOWN]:
        if(cat.y<359):
            cat.y += 5
            cat.rect.move(cat.x, cat.y)
            cat.rect = pygame.Rect(cat.x + 28, cat.y + 28, 100, 100)
    if pressed[pygame.K_LEFT]:
        if(cat.x>0):
            cat.x -= 5
            cat.rect.move(cat.x, cat.y)
            cat.rect = pygame.Rect(cat.x + 28, cat.y + 28, 100, 100)
    if pressed[pygame.K_RIGHT]:
        if(cat.x<512):
            cat.x +=5
            cat.rect.move(cat.x, cat.y)
            cat.rect = pygame.Rect(cat.x + 28, cat.y + 28, 100, 100)

    screen.fill([0,0,0])

    scary1.move()
    scary2.move()
    scary3.move()

    if(cooldown >= 60):
        if(cat.rect.colliderect(scary1)):
            collisions += 1
            cooldown = 0
            screen.fill([90, 0, 0])
        if(cat.rect.colliderect(scary2)):
            collisions += 1
            cooldown = 0
            screen.fill([90, 0, 0])
        if(cat.rect.colliderect(scary3)):
            collisions += 1
            cooldown = 0
            screen.fill([90, 0, 0])


    font = pygame.font.Font(None, 36)
    text = font.render("Collisions: ", 1, (90, 90, 90))
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)
    col = str(collisions)
    text2 = font.render(col, 1, (90,90,90))
    screen.blit(text2, (400, 0))

    screen.blit(cat.image, (cat.x,cat.y))
    screen.blit(scary1.image, (scary1.x, scary1.y))
    screen.blit(scary2.image, (scary2.x, scary2.y))
    screen.blit(scary3.image, (scary3.x, scary3.y))

    if(cooldown < 60):
        cooldown += 1

    pygame.display.flip()
    clock.tick(60)