import pygame
import random
import sys

def paintentity(entity,x,y):
    monitor.blit(entity, (x,y))

def writescore(score):
    txt=myfont.render(u'파괴한 우주괴물 수:'+str(score),True, (255-r,255-g,255-b))
    monitor.blit(txt,(10,sheight-40))

def playgame():
    global monitor, ship, monster,missile
    r=random.randrange(0,256)
    g=random.randrange(0,256)
    b=random.randrange(0,256)
    
    shipx=swidth/2
    shipy=sheight*0.8
    dx,dy=0,0
    
    
    monster=pygame.image.load(random.choice(monsterImage))
    monstersize=monster.get_rect().size
    monsterx=0
    monstery=random.randrange(0,int(swidth*0.3))
    monsterspeed=random.randrange(1,5)
    
    missilex,missiley=None,None
    
    firecount=0
    
    while True:
        (pygame.time.Clock()).tick(50)
        monitor.fill((r,g,b))
        
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
                
            if e.type in [pygame.KEYDOWN]:
                if e.key == pygame.K_LEFT : dx=-5
                elif e.key == pygame.K_RIGHT: dx=+5
                elif e.key == pygame.K_UP: dy=-5                
                elif e.key == pygame.K_DOWN: dy=+5
                elif e.key==pygame.K_SPACE:
                    if missilex==None:
                        missilex=shipx+shipsize[0]/2
                        missiley=shipy
            
            if e.type in [pygame.KEYUP]:
                 if e.key==pygame.K_LEFT or e.key==pygame.K_RIGHT \
                    or e.key == pygame.K_UP or e.key == pygame.K_DOWN : dx,dy=0,0
            
        if (0 < shipx + dx and shipx + dx <= swidth -shipsize[0]) \
            and (sheight/2 <shipy+dy and shipy + dy <= sheight -shipsize[1]):
            shipx +=dx
            shipy +=dy
                
        paintentity(ship,shipx,shipy)
        
        monsterx += monsterspeed
        if monsterx>swidth:
            monsterx=0
            monstery=random.randrange(0,int(swidth*0.3))
            monster=pygame.image.load(random.choice(monsterImage))
            monstersize=monster.get_rect().size
            monsterspeed=random.randrange(1,5)
            
        paintentity(monster,monsterx,monstery)
        
        if missilex !=None:
            missiley -=10
            if missiley <0:
                missilex, missiley = None, None
        if missilex !=None:
            paintentity(missile,missilex,missiley)
            
            if (monsterx < missilex and missilex<monsterx+monstersize[0]) and \
               (monstery < missiley and missiley<monstery + monstersize[1]):
                firecount +=1
                
                monster = pygame.image.load(random.choice(monsterImage))
                monstersize=monster.get_rect().size
                monsterx=0
                monstery=random.randrange(0,int(swidth*0.3))
                monsterspeed=random.randrange(1,5)
                
                missilex,missiley=None,None
                
        writescore(firecount)
            
        pygame.display.update()
        print('~',end='')
        
r,g,b=[0]*3
swidth,sheight=1400,1000
monitor=None
ship,shipsize=None,0

monsterImage=['i_weapon1.png','i_weapon2.png','i_weapon3.png',\
              'm_weapon1.png','m_weapon2.png','m_weapon3.png']
monster=None

missile=None

pygame.init()
monitor=pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship=pygame.image.load('background.png')
shipsize=ship.get_rect().size
missile=pygame.image.load('i_weapon2.png')

#playgame()
