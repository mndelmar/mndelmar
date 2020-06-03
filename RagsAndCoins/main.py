import pygame 
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()
screensize = (800, 600)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Rags and Groins')
icon = pygame.image.load("img/sword.png")
pygame.display.set_icon(icon)

bg = pygame.image.load('img/bg.png')
char = pygame.image.load('img/standing.png')

class Player():
    walkRight = [pygame.image.load('img/R1.png'), pygame.image.load('img/R2.png'), pygame.image.load('img/R3.png'), pygame.image.load('img/R4.png'), pygame.image.load('img/R5.png'), pygame.image.load('img/R6.png'), pygame.image.load('img/R7.png'), pygame.image.load('img/R8.png'), pygame.image.load('img/R9.png')]
    walkLeft = [pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L7.png'), pygame.image.load('img/L8.png'), pygame.image.load('img/L9.png')]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.isJump = False
        self.jumpCount = 17
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                screen.blit(self.walkLeft[self.walkCount//3],(self.x, self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(self.walkRight[self.walkCount//3],(self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(self.walkRight[0], (self.x, self.y))
            else:
                screen.blit(self.walkLeft[0], (self.x, self.y))


class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self, screen):
        pygame.draw.circle(screen,self.color, (self.x, self.y), self.radius)

class Enemy(object):
    walkRight = [pygame.image.load('img/R1E.png'), pygame.image.load('img/R2E.png'), pygame.image.load('img/R3E.png'), pygame.image.load('img/R4E.png'), pygame.image.load('img/R5E.png'), pygame.image.load('img/R6E.png'), pygame.image.load('img/R7E.png')] #pygame.image.load('img/R8E.png')# pygame.image.load('img/R9E.png'), pygame.image.load('img/R10E.png'), pygame.image.load('img/R11E.png')]
    walkLeft = [pygame.image.load('img/L1E.png'), pygame.image.load('img/L2E.png'), pygame.image.load('img/L3E.png'), pygame.image.load('img/L4E.png'), pygame.image.load('img/L5E.png'), pygame.image.load('img/L6E.png'), pygame.image.load('img/L7E.png')] #pygame.image.load('img/L8E.png') #pygame.image.load('img/L9E.png'), pygame.image.load('img/L10E.png'), pygame.image.load('img/L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]  # This will define where our enemy starts and finishes their path.
        self.walkCount = 0
        self.speed = 1
        

    def draw(self, screen):
        self.move()
        if self.walkCount + 1 >= 42:
            self.walkCount = 0
        if self.speed > 0:
            screen.blit(self.walkRight[self.walkCount//6], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(self.walkLeft[self.walkCount//6], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.speed > 0:
            if self.x < self.path[0] + self.speed:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.x += self.speed
                self.walkCount = 0
        else:
            if self.x > self.path[1] + self.speed:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.x += self.speed
                self.walkCount = 0

def reDrawGameWindow():
    screen.blit(bg, (0, 0))
    player.draw(screen)
    enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for bullet in bulletss:
        bullet.draw(screen)
    pygame.display.update()

#Mainloop
player = Player(400, 430, 64, 64)
enemy = Enemy(600, 435, 64, 64, 150)
bullets = []
bulletss = []
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))
    for bullet in bulletss:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bulletss.pop(bulletss.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT]:
        player.x += player.speed
        player.left = False
        player.right = True
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if keys[pygame.K_q]:
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 100:
            bullets.append(Projectile(round(player.x + player.width//2), round(player.y + player.height//2),10,(0,0,0),facing))

    if keys[pygame.K_w]:
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bulletss) < 100:
            bulletss.append(Projectile(round(player.x + player.width//2), round(player.y + player.height//2),10,(255,0,0),facing))

    if not (player.isJump):
        if keys[pygame.K_SPACE]: 
            player.isJump = True
            #player.left = False
            #player.right = False
            player.walkCount = 0
    else:       
        if player.jumpCount >= -17:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= round((player.jumpCount ** 2) * 0.1 * neg)
            player.jumpCount -= 1
            
        else:
            player.isJump = False
            player.jumpCount = 17   
       
    reDrawGameWindow()
    