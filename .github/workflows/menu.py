import pygame,objects,level_loader
def run(surface,img,liss):
    running=True
    main_screen=pygame.Surface((8000,2000))
    liss.load(objects.wall,8000,objects.ring,objects.spike,main_screen)
    x=0
    FPS=1000
    sonic = objects.player(main_screen,(128,128),liss.objs)
    clock=pygame.time.Clock()
    k=0
    time=0
    surface.set_alpha(None)
    main_screen.set_alpha(None)
    back=objects.background(main_screen,img,"sound/music.ogg",liss.objs)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                sonic.event(event)
                if event.key==pygame.K_p:
                    print "FPS Toggle"
                    if FPS ==1000:
                        FPS=60
                    elif FPS ==60 :FPS=1000
                    print FPS
                if event.key==pygame.K_ESCAPE:
                    running=False
            if event.type == pygame.KEYUP:
                
                sonic.re_event(event)
        
        x = -sonic.rect[0]
        y=sonic.rect[1]
        if x+300>0:
            x=-300
        if x-300<-7800:
            x=-7500
        if y-300<0:
            y=300
        if y-300>1400:
            y=1700
        surface.blit(main_screen,(x+300,-y+300))
        back.update(sonic.rect[0],sonic.rect[1])
        objects.writer(surface,10,9,"RINGS : "+str(sonic.rings),(0,0,0))
        objects.writer(surface,11,11,"RINGS : "+str(sonic.rings),(255,255,255))
        objects.writer(surface,10,32,"FPS : "+str(round(clock.get_fps(),0)),(0,0,0))
        objects.writer(surface,11,34,"FPS : "+str(round(clock.get_fps(),0)),(255,255,255))
        sonic.update()
        for i in liss.objs:
            i.update()
        pygame.display.update()
        clock.tick(FPS)
    return False
