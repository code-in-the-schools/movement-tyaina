import pygame
import os

image_path = os.path.join('chell.png')

class character(object):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            character.image = pygame.image.load("chell.png")
            self.image = character.image

            self.x = 50
            self.y = 50
            self.hitbox = (self.x,self.y,55,55)


        def draw(self, surface):
            surface.blit(self.image,(self.x,self.y))
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)

pygame.init()
screen_width = 600
screen_hieght = 600
screen = pygame.display.set_mode((screen_width,screen_hieght))

Sprite = character()
clock = pygame.time.Clock()

running = True
while running:
                # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
        screen.fill((255,255,255))
        Sprite.draw(screen)

        pygame.display.update()
        
        clock.tick(60)

def movement():
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
        if event.key == pygame.K_UP or event.key == ord('w'):
            print('jump')
        