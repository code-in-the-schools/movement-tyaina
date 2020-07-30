import pygame
import os

image_path = os.path.join('chell.png')

class Obstical(object):
 def __init__(self):
  character.image = pygame.image.load("chell.png")
  self.image = character.image
  self.image = pygame.transform.scale(self.image,(250,200))

class character(object):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            character.image = pygame.image.load("chell.png")
            self.image = character.image
            self.image = pygame.transform.scale(self.image,(250,200))

            self.x = 50
            self.y = 50
            self.hitbox = (self.x - 25,self.y - 25,55,55)


        def draw(self, surface):
            surface.blit(self.image,(self.x,self.y))
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                
        def movement(self, width, hight):
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and character.isHit(width,hight).l == False:
                self.x -= 1
            if key[pygame.K_RIGHT] and character.isHit(width,hight).r == False:
                self.x += 1
            if key[pygame.K_UP] and character.isHit(width,hight).u == False:
                self.y -= 1
            if key[pygame.K_DOWN] and character.isHit(width,hight).d == False:
                self.y += 1
        def gravity(self):
            if self.y > 0 and pygame.key.get_focused() == False:
               self.y += 1
        def isHit(width,hight):
            r,l,u,d = False
            if self.y > 0:
                self.u = True
                else:
                self.u = False
            if self.x > 0:
                self.l = True
                else:
                    self.l = False
            if self.y < hight - 50:
                self.d = True
                else:
                    self.d = False
            if self.x < width - 50:
                self.r = True
                else:
                    self.r =False


    pygame.init()
    screen_width = 600
    screen_hieght = 600
    screen = pygame.display.set_mode((screen_width,screen_hieght))

Sprite = character()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit() # quit the screen
        running = False
        screen.fill((255,255,255))
        
        Sprite.gravity(screen_hieght)
        Sprite.movement(screen_width,screen_hieght)
        
        Sprite.draw(screen)
     
        pygame.display.update()
        
        clock.tick(60)

def gravity(self):
    if self.y > 0 and pygame.key.get_focused() == False:
        self.y += 1

     