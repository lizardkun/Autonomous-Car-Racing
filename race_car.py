# Modules
import pygame
import time
import random


# Initiate pygame. Always needed
pygame.init() 

# Clock
clock = pygame.time.Clock()

# RGB Color
BLACK = (0,0,0)
RED = (255,0,0)

# window with size of 500 x 400 pixels
wn_width = 500
wn_height = 400
wn = pygame.display.set_mode((wn_width,wn_height))
pygame.display.set_caption('Race car with road block')

# image
bg = pygame.image.load('images/3lane.png')
carimg = pygame.image.load('images/porsche.png')
DEFAULT_IMAGE_SIZE=(wn_width,wn_height)
bg = pygame.transform.scale(bg, DEFAULT_IMAGE_SIZE)
CAR_SIZE=(60,100)
carimg = pygame.transform.scale(carimg, CAR_SIZE)

# boundary
west_b = 100
east_b = 380

class Block:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speedy = 5
        self.dodged = 0
        
    def update(self):
        self.y = self.y + self.speedy
       # check boundary (block)
        if self.y > wn_height:
           self.y = 0 - self.height
           self.x = random.randrange(west_b,east_b-self.width)

           self.dodged = self.dodged + 1

    def draw(self,wn):
        pygame.draw.rect(wn, RED, [self.x, self.y, self.width, self.height])
                  
class Player:
    def __init__(self):
        self.image = carimg
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.rect = self.image.get_rect()
        self.rect.x = int(wn_width * 0.5)
        self.rect.y = int(wn_height * 0.5)
        
        self.speedx = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        
        self.rect.x = self.rect.x + self.speedx        

       # check boundary (west)
        if  self.rect.left < west_b:
           self.rect.left = west_b
       # check boundary (east)
        if  self.rect.right > east_b:
           self.rect.right = east_b

# Functions
def score_board(dodged):
    font = pygame.font.Font(None,25)
    text = font.render('Dodged: ' + str(dodged),True,BLACK)
    wn.blit(text,(0,0)) 

def crash():
    font = pygame.font.Font(None,80) 
    text = font.render('You crashed!',True,BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    x = int(wn_width/2-text_width/2)
    y = int(wn_height/2-text_height/2)
    wn.blit(text,(x,y))
    pygame.display.update()
    time.sleep(2)
    game_loop()


# def game function 
def game_loop():
    
    block_width = 80
    block_height = 20
    block_x = random.randrange(west_b, east_b - block_width)
    block_y = -100

    player = Player()
    block = Block(block_x,block_y,block_width,block_height)
    
    while True:
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()

       player.update()
       block.update()

       wn.blit(bg,(0,0)) # (0,0)location on the wn
       wn.blit(player.image,(player.rect.x,player.rect.y))
       block.draw(wn)
       
       # Car collision with block 
       if player.rect.right > block.x and player.rect.x < block.x + block.width:
           if block.y + block.height > player.rect.y and block.y < player.rect.bottom:
              crash()

##       # Score
       score_board(block.dodged)
          
       pygame.display.update()
       clock.tick(60) 
       


### pygame quit
game_loop()
pygame.quit()
quit()