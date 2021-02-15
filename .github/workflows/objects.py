import pygame;import Spritesheet
ss = Spritesheet.spritesheet("images/sprite_sheet.png")
sr=Spritesheet.spritesheet("images/BGObjects.gif")
pygame.mixer.init()
class player:
    surface=None
    img=None
    images=[]
    speedx=0
    keyal=0
    speedy=0
    rect=None
    wall =[]
    spin=False
    rings=0
    grounded=False
    speedh=0
    rstay=False
    spind=False
    hit=False
    k=8
    n=0
    look_up=False
    look_down=False
    Swrong=pygame.mixer.Sound("sound/wrong.wav")
    Sjump=pygame.mixer.Sound("sound/jump.wav")
    Sring=pygame.mixer.Sound("sound/ring.wav")
    relase=pygame.mixer.Sound("sound/down.wav")
    Spinddash=pygame.mixer.Sound("sound/spind.wav")
    sDownkey=pygame.mixer.Sound("sound/downkey.wav")
    d=0
    rd=0
    hurt=False
    direction=2
    out=True
    wall_out=False
    def __init__(self,surface,pos,wall):
        self.surface=surface
        self.load_sprites()
        self.img=self.images[0]
        self.rect=self.img.get_rect()
        self.rect[0]=pos[0]
        self.rect[1]=pos[1]
        self.wall=wall
    def load_sprites(self):
        self.image_correct([1,2,29,39],(0,128,128))#0,1 stand
        #------------------------------------------------------
        self.image_correct([1,44,39,40],(0,128,128))#2,3 move
        self.image_correct([41,45,39,39],(0,128,128))#4,5 move
        self.image_correct([81,46,26,46],(0,128,128))#6,7 move
        self.image_correct([108,44,28,40],(0,128,128))#8,9 move
        self.image_correct([137,44,37,40],(0,128,128))#10,11 move
        self.image_correct([175,45,38,39],(0,128,128))#12,13 move
        self.image_correct([214,45,26,39],(0,128,128))#14,15 move
        self.image_correct([241,44,26,40],(0,128,128))#16,17 move
        #______________________________________________
        self.image_correct([268,45,32,39],(0,128,128))#18,19 run
        self.image_correct([301,45,32,39],(0,128,128))#20,21 run
        self.image_correct([334,45,31,39],(0,128,128))#22,23 run
        self.image_correct([366,45,32,39],(0,128,128))#24,25 run
        #______________________________________________
        self.image_correct([1,512,36,39],(0,128,128))#26,27 stoping
        self.image_correct([38,512,35,39],(0,128,128))#28,29 stoping
        self.image_correct([74,512,32,39],(0,128,128))#30,31 stoping
       #______________________________________________
        self.image_correct([1,140,30,39],(0,128,128))#32,33 jumping
        self.image_correct([32,140,30,39],(0,128,128))#34,35 jumping
        self.image_correct([63,140,30,39],(0,128,128))#36,37 jumping
        self.image_correct([94,140,30,39],(0,128,128))#38,39 jumping
        self.image_correct([126,140,30,39],(0,128,128))#40,41 jumping
        #______________________________________________
        self.image_correct([420,1,32,40],(0,128,128))#42,43 look_up
        self.image_correct([453,2,35,39],(0,128,128))#44,45 look_up
        #______________________________________________
        self.image_correct([489,2,24,39],(0,128,128))#46,47 look_down
        self.image_correct([514,2,27,39],(0,128,128))#48,49 look_down
        #______________________________________________
        self.image_correct([158,140,30,39],(0,128,128))#50,51 spindash
        self.image_correct([189,140,29,39],(0,128,128))#52,53 spindash
        self.image_correct([219,140,29,39],(0,128,128))#54,55 spindash
        self.image_correct([249,140,29,39],(0,128,128))#56,57 spindash
        self.image_correct([279,140,29,39],(0,128,128))#58,59 spindash
        self.image_correct([308,140,29,39],(0,128,128))#60,61 spindash
        #_____________________________________________
        self.image_correct([267,553,28,39],(0,128,128))#62,63 wall_pushing
        self.image_correct([296,553,24,39],(0,128,128))#64,65 wall_pushing
        self.image_correct([321,553,28,39],(0,128,128))#66,67 wall_pushing
        self.image_correct([350,553,24,39],(0,128,128))#68,69 wall_pushing
        #______________________________________________
        self.image_correct([37,553,38,39],(0,128,128))#70,71 Hurt
        self.image_correct([76,553,39,39],(0,128,128))#72,73 Hurt        
    def image_correct(self,rect,color):
        image=pygame.transform.scale(ss.image_at(rect,color),(rect[2]*2,rect[3]*2))
        self.images.append(image)
        image=pygame.transform.flip(image,1,0)
        self.images.append(image)
    def hurts(self):
        self.speedy=0
        self.speedy=-8
        self.speedx=0
        if self.direction==1 or self.direction==3:
            self.speedx=7
        if self.direction==0 or self.direction ==2:
            self.speedx=-7
        self.hurt=True
    def update(self):
        self.run()
        if self.spind==True:
            self.spindash()
        self.sprite_update()
        if self.direction ==2 or self.direction ==3:
                        self.wall_out=False                    
        self.surface.blit(self.img,self.rect)
        self.rect[0]+=self.speedx
        hitx = pygame.sprite.spritecollide(self,self.wall,False)        
        for hit in hitx:            
            if hit.idd =="wall":
                self.hurt=False
                if self.speedx>0:
                    self.rect.right=hit.rect.left
                    self.speedx=0
                    self.stop()
                    if self.direction==0 or self.direction ==1:
                        self.wall_out=True
                if self.speedx<0:
                    self.rect.left=hit.rect.right
                    self.speedx=0
                    self.stop()
                    if self.direction==0 or self.direction ==1:
                        self.wall_out=True                
            if hit.idd=="ring":
                if hit.dell==False:
                    self.Sring.play()
                    hit.dell=True
                    self.rings+=1
            if hit.idd =="spike":
                if hit.di ==0:
                    if self.hurt == False:
                        if self.speedx>0:
                            self.rect.right=hit.rect.left
                            self.speedx=0
                            self.stop()
                            if self.direction==0 or self.direction ==1:
                                self.wall_out=True
                        if self.speedx<0:
                            self.rect.left=hit.rect.right
                            self.speedx=0
                            self.stop()
                            if self.direction==0 or self.direction ==1:
                                self.wall_out=True
                if hit.di==1:                
                    self.hurts()
                    self.grounded=False    
        self.rect[1]+=self.speedy
        self.gravity()
        hity = pygame.sprite.spritecollide(self,self.wall,False)
        if len(hity)>0:
            self.hit=True
        else:self.hit=False
        for hit in hity:
            if hit.idd =="wall":
                self.hurt=False
                if self.speedy>0 and self.rect[1] < hit.rect[1]:                    
                    self.rect.bottom=hit.rect.top
                    self.grounded=True
                if self.speedy<0 :                   
                    self.rect.top=hit.rect.bottom
                    self.speedy=-self.speedy
            if hit.idd=="ring":
                if hit.dell==False:
                    self.Sring.play()
                    hit.dell=True
                    self.rings+=1
            if hit.idd == "spike":
                if hit.di==1:
                    if self.hurt==False:
                        if self.speedy>0 and self.rect[1] < hit.rect[1]:                    
                            self.rect.bottom=hit.rect.top
                            self.grounded=True
                        if self.speedy<0 :                   
                            self.rect.top=hit.rect.bottom
                            self.speedy=-self.speedy
                if hit.di==0:
                        
                    if self.speedy>0 :
                        self.hurts()
                        self.grounded=False
                    if self.speedy<0 :
                        self.grounded=False
                        self.hurts()               
    def gravity(self):
        if self.grounded==False:
            self.speedy+=0.44
        if self.grounded==True:
            self.speedy+=0.44
            if self.speedy>10:
                self.speedy=0.44
            if self.speedy >1.6 and self.hit==False:
                self.grounded=False
    def event(self,event):
        if event.key== pygame.K_RIGHT:
            if self.rstay==False:
                self.direction=0
                self.keyal=1
                self.rd=0
        if event.key == pygame.K_LEFT:
            if self.rstay==False:
                self.direction=1
                self.keyal=1
                self.rd=1
        if event.key == pygame.K_SPACE:
            if self.look_down == False:
                self.wall_out=False
                self.jump()
            if self.look_down==True and self.hurt == False:
                self.rstay=True
                self.spind=True
                self.Spinddash.play()                
                if self.speedh<1:
                    self.speedh+=9
                if self.speedh>8:
                    self.speedh+=4
                if self.speedh>28:
                    self.speedh=28
        if event.key == pygame.K_UP:
            self.look_up=True
        if event.key == pygame.K_DOWN:
            self.look_down=True            
            self.spin=True
    def re_event(self,event):
        if event.key== pygame.K_RIGHT:
            self.direction=2
            self.keyal=0 
        if event.key == pygame.K_LEFT:
            self.direction=3
            self.keyal=0
        if event.key == pygame.K_UP:
            self.look_up=False
        if event.key == pygame.K_DOWN:
            self.look_down=False
            if self.rstay==True:
                self.relase.play()
                self.spin=True
                self.rstay=False
##        if event.key == pygame.K_SPACE:
##            if self.spind==True:
##                self.spind=False
##                self.stop()            
    def run(self):
        if self.direction==0:
            self.speedx+=0.10
            if self.speedx > 14:
                self.speedx=14
            if self.speedx<-4:
                self.speedx=-4                
                self.spin=False
                self.speedh=0
            if self.speedx<0:
                if self.grounded==True:
                    self.Swrong.play()
        if self.direction==1:
            self.speedx-=0.10
            if self.speedx < -14:
                self.speedx=-14
            if self.speedx>4:
                self.speedx=4
                self.spin=False
                self.speedh=0
            if self.speedx>0:
                if self.grounded==True:
                    self.Swrong.play()
        if self.direction==2 or self.direction ==3:
            self.stop()
    def spindash(self):
        if self.spind==True and self.look_down==False and self.hurt==False:
            if self.direction==2:
                self.speedx+=self.speedh
                self.stop()
                self.spind=False
            if self.direction==3:
                self.speedx-=self.speedh
                self.stop()
                self.spind=False
    def jump(self):
        if self.grounded==True:
            self.speedy=0
            self.Sjump.play()
            self.grounded=False
            self.speedy-=13
    def get_ring(self,hit):
        self.out=False
        del hit
    def sprite_update(self):
        walking_right_cycle=[2,4,6,8,10,12,14,16]
        run_right_cycle=[18,20,22,24]
        jump_right_cycle=[32,34,36,38,40]
        jump_left_cycle=[33,35,37,39,41]
        look_up_right_cycle=[42,44]
        look_down_right_cycle=[46,48]
        look_down_left_cycle=[47,49]
        look_up_left_cycle=[43,45]
        stop_right_cycle=[26,28,30]
        stop_left_cycle=[27,29,31]
        run_left_cycle=[19,21,23,25]
        spindash_right_cycle=[50,52,54,56,58,60]
        wall_right_cycle=[62,64,66,68]
        wall_left_cycle=[63,65,67,69]
        spindash_left_cycle=[51,53,55,57,59,61]
        walking_left_cycle=[3,5,7,9,11,13,15,17]
        hurt_right_cycle=[70,72]
        hurt_left_cycle=[71,73]
        if self.rd ==0:            
            if self.grounded==True:
                if self.speedx==0:
                    self.spin=False
                    self.img=self.images[0]
                    if self.look_up==True:
                        if self.d>1:self.d=0
                        if self.d==1:self.img = self.images[look_up_right_cycle[self.d]]
                        if self.d==0:
                            self.img = self.images[look_up_right_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                    if self.look_down == True and self.rstay==False and self.wall_out==False:
                        if self.d>1:self.d=0
                        if self.d==1:self.img = self.images[look_down_right_cycle[self.d]]
                        if self.d==0:
                            self.img = self.images[look_down_right_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                    if self.rstay == True:
                        if self.d>5:self.d=0
                        self.img = self.images[spindash_right_cycle[self.d]]
                        self.n+=1
                        if self.n == self.k:
                            self.d+=1
                            self.n=0
                if self.keyal==1 or self.spin==False:
                    if self.wall_out == True:
                        if self.d>3:self.d=0
                        self.img = self.images[wall_right_cycle[self.d]]
                        self.n+=1
                        if self.n == self.k:
                            self.d+=1
                            self.n=0
                    else:
                        if self.speedx>0 and self.speedx < 8:
                            if self.d>7:self.d=0
                            self.img = self.images[walking_right_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                        if self.speedx>9:
                            if self.d>3:self.d=0
                            self.img = self.images[run_right_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                    if self.speedx<0:
                        if self.grounded==True:
                            if self.d>2:self.d=0
                            self.img = self.images[stop_left_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                if self.speedx>0 and self.spin==True and self.keyal==0:
                    if self.d>3:self.d=0
                    self.img = self.images[jump_right_cycle[self.d]]
                    self.n+=1
                    if self.n == self.k:
                        self.d+=1
                        self.n=0
            if self.grounded==False:
                if self.hurt==False:
                    if self.d>3:self.d=0
                    self.img = self.images[jump_right_cycle[self.d]]
                    self.n+=1
                    if self.n == self.k:
                        self.d+=1
                        self.n=0
                if self.hurt==True:
                    if self.d>1:self.d=0
                    self.img = self.images[hurt_right_cycle[self.d]]
                    self.n+=1
                    if self.n == self.k:
                        self.d+=1
                        self.n=0
        if self.rd==1:
            if self.grounded == True:
                if self.speedx==0:
                    self.spin=False
                    self.img=self.images[1]
                    if self.look_up==True:
                        if self.d>1:self.d=0
                        if self.d==1:self.img = self.images[look_up_left_cycle[self.d]]
                        if self.d==0:
                            self.img = self.images[look_up_left_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                    if self.look_down == True and self.rstay==False:
                        if self.d>1:self.d=0
                        if self.d==1:self.img = self.images[look_down_left_cycle[self.d]]
                        if self.d==0:
                            self.img = self.images[look_down_left_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                    if self.rstay == True:
                        if self.d>5:self.d=0
                        self.img = self.images[spindash_left_cycle[self.d]]
                        self.n+=1
                        if self.n == self.k:
                            self.d+=1
                            self.n=0
                if self.keyal==1 or self.spin==False:
                    if self.wall_out == True:
                        if self.d>3:self.d=0
                        self.img = self.images[wall_left_cycle[self.d]]
                        self.n+=1
                        if self.n == self.k:
                            self.d+=1
                            self.n=0
                    else:
                        if self.speedx<0 and self.speedx > -8:
                            if self.d>7:self.d=0
                            self.img = self.images[walking_left_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                        if self.speedx < -9:
                            if self.d>3:self.d=0
                            self.img = self.images[run_left_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                        if self.speedx>0:
                            if self.d>2:self.d=0
                            self.img = self.images[stop_right_cycle[self.d]]
                            self.n+=1
                            if self.n == self.k:
                                self.d+=1
                                self.n=0
                if self.speedx<0 and self.spin==True and self.keyal==0:
                    if self.d>3:self.d=0
                    self.img = self.images[jump_left_cycle[self.d]]
                    self.n+=1
                    if self.n == self.k:
                        self.d+=1
                        self.n=0
            if self.grounded==False:
                if self.hurt==False:
                    if self.d>3:self.d=0
                    self.img = self.images[jump_left_cycle[self.d]]
                    self.n+=1
                    if self.n == self.k:
                        self.d+=1
                        self.n=0
                if self.hurt==True:
                    if self.d>1:self.d=0
                    self.img = self.images[hurt_left_cycle[self.d]]
                    self.n+=1
                    if self.n == self.k:
                        self.d+=1
                        self.n=0
    def stop(self):
        if self.speedx>0:
            if self.spin==False:
                self.speedx-=0.25
                if self.speedx<0:
                    self.speedx=1
                    self.speedx=0
            if self.spin==True:
                self.speedx-=0.1
                if self.speedx<0:
                    self.speedx=1
                    self.speedx=0
            self.rstay=False
        if self.speedx<0:
            if self.spin ==False:
                self.speedx+=0.25
                if self.speedx>0:
                    self.speedx=-1
                    self.speedx=0
                    self.speedh=0
            if self.spin==True:
                self.speedx+=0.1
                if self.speedx>0:
                    self.speedx=-1
                    self.speedx=0
                    self.speedh=0
class wall:
    surface=None
    img=None
    idd="wall"
    rect=None
    bit =False
    k=12
    n=0
    def __init__(self,img,surface,pos):
        self.surface = surface
        self.img = img
        self.rect = self.img.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
    def update(self):
        if self.bit==True:
            self.surface.blit(self.img,self.rect)
            self.n+=1
            if self.k == self.n:
                self.n=0
                self.bit=False
class background:
    surface=None
    rect=[]
    img=None
    load=1
    wall=[]
    Rmusic=None
    def __init__(self,surface,img,music,walls):
        self.surface=surface
        self.wall=walls
        self.img =img
        self.Rmusic=music
        self.rect = pygame.Rect(0,0,850,650)
    def update(self,x,y):
        if self.load ==1:
            self.img = pygame.transform.scale(self.img,(self.rect[2],self.rect[3]))
            self.load=0
            pygame.mixer.music.load(self.Rmusic)
            pygame.mixer.music.set_volume(50)
            pygame.mixer.music.play(-1)
        self.rect[0]=x-(self.rect[2]*0.375)
        if self.rect[0] <0:
            self.rect[0]=0
        if self.rect[0]+self.rect[2] >8000:
            self.rect[0] = -1*(self.rect[2]-8000)
            print self.rect[0]
        hity = pygame.sprite.spritecollide(self,self.wall,False)
        for hit in hity:
                    hit.bit=True
        
        self.rect[1]=y-(self.rect[3]*0.50)
        if self.rect[1]+self.rect[3]>2000:
            self.rect[1]=-1*(self.rect[3]-2000)
        if self.rect[1] <0:
            self.rect[1]=0
        hity = pygame.sprite.spritecollide(self,self.wall,False)
        for hit in hity:
                    hit.bit=True
        pygame.draw.rect(self.surface,(255,0,0),self.rect,2)
        self.surface.blit(self.img,self.rect)
class ring:
    surface=None
    img=None
    d=0
    n=0
    m=0
    p=12
    rect=[]
    k=7
    bit=False
    dell=False
    pos=(0,0)
    idd="ring"
    image_list=[]
    def __init__(self,surface,pos):
        self.surface=surface
        self.pos=pos
        self.load()
    def update(self):
        if self.d >3:self.d=0
        if self.dell==False:
            if self.bit==True:
                self.surface.blit(self.image_list[self.d],self.pos)
                self.m+=1
                if self.m == self.p:
                    self.m=0
                    self.bit=False
                
        self.n+=1
        if self.n == self.k:
            self.n=0
            self.bit=False
            self.d+=1
    def load(self):
        self.image_list.append(pygame.transform.scale(sr.image_at([10,63,16,16],colorkey=(0,140,189)),(32,32)))
        self.image_list.append(pygame.transform.scale(sr.image_at([50,63,12,16],colorkey=(0,140,189)),(24,32)))
        self.image_list.append(pygame.transform.scale(sr.image_at([35,63,6,16],colorkey=(0,140,189)),(12,32)))
        self.image_list.append(pygame.transform.scale(sr.image_at([70,63,12,16],colorkey=(0,140,189)),(24,32)))
        self.rect=self.image_list[0].get_rect()
        self.rect[0]=self.pos[0]
        self.rect[1]=self.pos[1]
def writer(surface,x,y,text,color):
    pygame.font.init()
    font=pygame.font.Font("fonts/HAMMERHEAD.otf",24)
    image=font.render(text,True,color)
    surface.blit(image,(x,y))
class spike:
    img=None
    surface=None
    idd="spike"
    bit=False
    di=None
    n=0
    k=14
    rect=None
    def __init__(self,surface,pos,di):
        self.surface = surface
        self.di =di
        self.load()
        
        self.rect[0]=pos[0]+2
        self.rect[1]=pos[1]
        
    def update(self):
        if self.bit==True:
                
            self.surface.blit(self.img,self.rect)
            self.n+=1
            if self.k == self.n:
                self.n=0
                self.bit=False
    def load (self):
        if self.di==0:
            self.img = pygame.transform.scale(sr.image_at([10,221,31,32],colorkey=(0,140,189)),(62,64))
        if self.di==1:
            self.img = pygame.transform.scale(sr.image_at([54,222,32,31],colorkey=(0,140,189)),(62,64))
        self.rect = self.img.get_rect()
class ring_fallen:
    surface=None
    img=None
    d=0
    n=0
    rect=[]
    k=7
    dell=False
    pos=(0,0)
    idd="ring"
    image_list=[]
    wall=None
    def __init__(self,surface,pos,wall):
        self.surface=surface
        self.pos=pos
        self.load()
    def update(self):
        if self.d >3:self.d=0
        if self.dell==False:
            self.surface.blit(self.image_list[self.d],self.pos)
        self.n+=1
        if self.n == self.k:
            self.n=0
            self.d+=1
    def load(self):
        self.image_list.append(pygame.transform.scale(sr.image_at([10,63,16,16],colorkey=(0,140,189)),(32,32)))
        self.image_list.append(pygame.transform.scale(sr.image_at([50,63,12,16],colorkey=(0,140,189)),(24,32)))
        self.image_list.append(pygame.transform.scale(sr.image_at([35,63,6,16],colorkey=(0,140,189)),(12,32)))
        self.image_list.append(pygame.transform.scale(sr.image_at([70,63,12,16],colorkey=(0,140,189)),(24,32)))
        self.rect=self.image_list[0].get_rect()
        self.rect[0]=self.pos[0]
        self.rect[1]=self.pos[1]
