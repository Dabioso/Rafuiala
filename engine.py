import pygame
from textures import Player_Textures
pygame.init()

screen_width = 928
screen_height = 793
screen = pygame.display.set_mode(size=(screen_width, screen_height))
title = pygame.display.set_caption('Rafuiala')
background = pygame.image.load('textures\\backgrounds\\forest.png')
fps = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height, speed, character, player_number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.isJumping = False
        self.jumpCount = 8
        self.standing = True
        self.left = False
        self.right = False
        self.walkCount = 0
        self.attackCount = 0
        self.character = character
        self.player_number = player_number
        self.isAttacking = False


    def movement(self):
        key = pygame.key.get_pressed()
        if self.player_number == 2:
            if self.isJumping == False:
                if key[pygame.K_UP]:
                    self.isJumping = True
                    self.standing = False
                    self.right = False      
                    self.left = False
                    self.walkCount = 0
            else:
                if self.jumpCount >= -8:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2) * 0.5 * neg
                    self.jumpCount -= 1
                else:
                    self.isJumping = False
                    self.jumpCount = 8
            if key[pygame.K_KP1]:
               self.standing = False
               self.isAttacking = True
            if key[pygame.K_LEFT] and self.x + (self.width//2) > 0: 
                self.x -= (self.speed + 5)
                if not self.isJumping:
                     self.standing = False
                     self.left = True
                     self.right = False
            elif key[pygame.K_RIGHT] and self.x + self.width < screen_width:
                self.x += self.speed
                if not self.isJumping:
                    self.standing = False
                    self.left = False
                    self.right = True
            elif not self.isJumping and not self.isAttacking:
                self.standing = True
                self.left = False
                self.right = False
                self.attack = False
                self.isAttacking = False
        elif self.player_number == 1:
            if self.isJumping == False:
                if key[pygame.K_w]:
                    self.isJumping = True
                    self.standing = False
                    self.right = False
                    self.left = False
                    self.walkCount = 0
            else:
                if self.jumpCount >= -8:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2) * 0.5 * neg
                    self.jumpCount -= 1
                else:
                    self.isJumping = False
                    self.jumpCount = 8
            if key[pygame.K_a] and self.x + (self.width//2) > 0: 
                self.x -= self.speed
                if not self.isJumping:
                    self.standing = False
                    self.left = True
                    self.right = False
            elif key[pygame.K_d] and self.x + self.width < screen_width:
                self.x += self.speed + 5
                if not self.isJumping:
                    self.standing = False
                    self.left = False
                    self.right = True
            elif not self.isJumping:    
                self.standing = True
                self.left = False
                self.right = False


    def draw(self, screen):
        standing, jumping, run, walk, attack = Player_Textures(self.character)

        if self.walkCount + 1 >= 21:
            self.walkCount = 0
        if self.attackCount + 1 >= 21:
             self.attackCount = 0
             self.isAttacking = False
             if not self.isJumping:
                self.standing = True
        if self.isJumping == True:
            if not self.isAttacking:
                screen.blit(jumping[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        if not self.isAttacking and not self.standing:
            if self.player_number == 1:
                if self.right:
                    screen.blit(run[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 3
                if self.left:
                    screen.blit(walk[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 3
            else:
                if self.right:
                    screen.blit(walk[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 3
                if self.left:
                    screen.blit(run[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 3
        elif not self.standing:
            screen.blit(attack[self.attackCount//3], (self.x, self.y))
            self.attackCount += 3
        else:
            screen.blit(standing[self.walkCount//3], (self.x, self.y))
            self.walkCount += 3


def redrawGameScreen():
    screen.blit(background, (0,0))
    knight.draw(screen)
    pirate.draw(screen)
    pygame.display.update()


knight = Player(100, 610, 200, 167, 3, "Knight", 1)
pirate = Player(464, 580, 200, 167, 5, "Pirate", 2)
