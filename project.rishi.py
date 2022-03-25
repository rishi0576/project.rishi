
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))
carrot_img = pygame.image.load("carrot.png").convert_alpha()
brinjal_img = pygame.image.load("brinjal.png").convert_alpha()
mushroom_img = pygame.image.load("mushroom.png").convert_alpha()
pumpkin_img = pygame.image.load("pumpkin.png").convert_alpha()
tomato_img = pygame.image.load("tomato.png").convert_alpha()
#creating objects of game
tomatoes=[]
mushrooms=[]
carrots=[]
brinjals=[]
pumpkins=[]

for i in range(1,6):
    tomatoes.append(pygame.Rect(i*60,50,40,40))

        
while True:    
    screen.fill((30,80,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             
    for tomato in tomatoes:        
        screen.blit(tomato_img,tomato)
    for carrot in carrots:        
        screen.blit(carrot_img,carrot)
    for brinjal in brinjals:        
        screen.blit(brinjal_img,brinjal)
    for mushroom in mushrooms:        
        screen.blit(mushroom_img,mushroom)
    for pumpkin in pumpkins:        
        screen.blit(pumpkin_img,pumpkin)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    pygame.display.update()
    clock.tick(30)

