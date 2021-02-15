import pygame,json,Spritesheet
class level:
    level=[]
    objs=[]
    surface=None
    image=None
    sizetile=None
    sizex=None
    sizey=None
    ss=None
    image_list=[0,0]
    def __init__(self,levelrr):
        filee =open(levelrr,'r')
        strings =filee.read()
        level =json.loads(strings)
        self.level= level['layers'][0]['data']
        self.image= level["tilesets"][0]["image"]
        self.sizetile= level["tilesets"][0]["tileheight"]
        self.sizey= level["tilesets"][0]["imageheight"]
        self.sizex= level["tilesets"][0]["imagewidth"]
        self.ss= Spritesheet.spritesheet(self.image)

    def load(self,claff,levelsizex,ring,spike,surface):
        self.surface=surface
        x=0
        y=0
        for f in self.level:
            if x ==levelsizex:
                x=0
                y+=self.sizetile
                
            if f==0:
                pass
            if f!=0:
                if f==4:
                    d=ring(self.surface,(x,y))
                    self.objs.append(d)
                elif f==5:
                    d = spike(self.surface,(x,y),0)
                    self.objs.append(d)
                elif f==6:
                    d = spike(self.surface,(x,y),1)
                    self.objs.append(d)
                else:
                    d=claff(self.image_list[f+1],self.surface,(x,y))
                    self.objs.append(d)
                
            x+=self.sizetile
            #print (x,y)
    def load_image(self):
        x=0
        y=-self.sizetile
        amount = self.sizex/self.sizetile
        amounty = self.sizey/self.sizetile
        for a2 in range (0,amounty):
            y+=self.sizetile
            x=0
            for f in range(0,amount):
                image=self.ss.image_at([x,y,self.sizetile,self.sizetile])
                self.image_list.append(image.convert())
                x+=self.sizetile
                
        
