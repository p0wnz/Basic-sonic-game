import pygame;import menu,sys,objects,level_loader,os
from pygame.locals import *

flags =  DOUBLEBUF
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption('Sonic_game')
screen=pygame.display.set_mode((800,600),flags)
running =True
menu_run=True
img=pygame.image.load("images/mushmush.png").convert()
levele=level_loader.level("level.json")
levele.load_image()
while running:
    running=menu.run(screen,img,levele)

pygame.quit()
sys.exit()

