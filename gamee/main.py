import pygame
import random
pygame.init()
x=0
sd=0
moveRight=False
moveLeft=False
moveUp=False

moveDown=False
myFont = pygame.font.SysFont( "생존", 30, True, False)
myFont1 = pygame.font.SysFont( "생존", 60, True, False)
y=350
CHA=[pygame.transform.scale(pygame.image.load('assets/1.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/1.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/2.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/3.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/4.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/5.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/6.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/7.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/8.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/9.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/10.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/11.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/1.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/2.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/3.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/4.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/5.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/6.png'), (80, 83)),
     pygame.transform.scale(pygame.image.load('assets/7.png'), (80, 83))]
bull = pygame.transform.scale(pygame.image.load('assets/b2.png'), (28, 12))
bull1 = pygame.transform.scale(pygame.image.load('assets/b1.png'), (28, 12))
bull2 = pygame.transform.scale(pygame.image.load('assets/b3.png'), (20, 20))
zom1 = pygame.transform.scale(pygame.image.load('assets/0.1.png'), (80, 83))
zom11 = pygame.transform.scale(pygame.image.load('assets/0.2.png'), (80, 83))
zom2 = pygame.transform.scale(pygame.image.load('assets/1.1.png'), (80, 83))
zom22 = pygame.transform.scale(pygame.image.load('assets/1.2.png'), (80, 83))
zom3 = pygame.transform.scale(pygame.image.load('assets/2.1.png'), (80, 83))
zom33 = pygame.transform.scale(pygame.image.load('assets/2.2.png'), (80, 83))
zom4 = pygame.transform.scale(pygame.image.load('assets/3.1.png'), (80, 83))
zom44 = pygame.transform.scale(pygame.image.load('assets/3.2.png'), (80, 83))
zom5 = pygame.transform.scale(pygame.image.load('assets/4.1.png'), (80, 83))
zom55 = pygame.transform.scale(pygame.image.load('assets/4.2.png'), (80, 83))
zom6 =pygame.transform.scale(pygame.image.load('assets/5.1.png'), (80, 83))
zom66=pygame.transform.scale(pygame.image.load('assets/5.2.png'), (80, 83))
zom7=pygame.transform.scale(pygame.image.load('assets/6.1.png'), (80, 83))
zom77=pygame.transform.scale(pygame.image.load('assets/6.2.png'), (80, 83))
size  = [1000,700]
screen= pygame.display.set_mode(size)
pygame.display.set_caption("Walking test")
done= False
k=0
ad=0
ggh=20
ggg=30
hhh=40
clock= pygame.time.Clock()
p=0
a=[]
bullet = []
en=[]
bc = 1
lkk=100
jkk=0
bnn=1
bulletc=20
ghh=10
edc=98  #97
dfg=100
zh=1
asxz=[]
xx = [0, 1000]
gameover=0
zd=1
MOVESPEED=8
mhp = 1
stagem = 0
while not done:
    if gameover == 0:
        text_title22 = myFont.render(str(lkk), True, (0,0,0))
        screen.blit(text_title22,(400,10))
        clock.tick(30)
        screen.fill((255, 255, 255))
        keys= pygame.key.get_pressed()
        text_title2 = myFont.render(str('round1'), True, (0,0,0))
        screen.blit(text_title2,(400,10))
        text_title2 = myFont.render(str(jkk), True, (0,0,0))
        screen.blit(text_title2,(600,10))
        if keys[ord('d')]==False and keys[ord('a')]==False:
            if p==0:
                screen.blit(CHA[k%19], (x, y))
                screen.blit(CHA[k%19], (x+20, y))
            if p==1:
                screen.blit(pygame.transform.flip(CHA[k%19], True, False), (x, y))
        if keys[ord('d')]:
            p=0
            k+=1
            sd=1
            screen.blit(CHA[k%19], (x, y))
        if keys[ord('a')]:
            k+=1
            p=1
            sd=0
            screen.blit(pygame.transform.flip(CHA[k%19], True, False), (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bc==1:
                        bulletc=bulletc-1
        ##                if bulletc == 0:
        ##                    bulletc = 0
                        if sd == 1:
                           bullet.append([x+50,y+50, 1])
                        else:
                            bullet.append([x+50,y+50, 0])
                if event.key == ord('a'):
                        moveLeft = True
                        moveRight = False
                if event.key == ord('w'):
                        moveUp = True
                        moveDown = False
                if event.key == ord('s'):
                        moveDown = True
                        moveUp = False
                if event.key == ord('d') :
                        moveRight = True
                        moveLeft = False
            if event.type==pygame.KEYUP:
                if event.key == ord('a'):
                        moveLeft = False
                if event.key == ord('d') :
                        moveRight = False
                if event.key == ord('w'):
                        moveUp = False
                if event.key == ord('s'):
                        moveDown = False
        
        if moveLeft:
            x -= MOVESPEED
        if moveRight:
            x += MOVESPEED
        if x>1050:
            x = x-MOVESPEED
            x=-50
        if x<-50:
            x=x+MOVESPEED
            x=1040
    ####################
        if moveUp:
            y -= MOVESPEED
        if moveDown:
            y += MOVESPEED
        if y>700:
            y = y-MOVESPEED
            y=-50
        if y<-50:
            y=y+MOVESPEED
            y=700
        CHA_rect = CHA[k%19].get_rect()
        CHA_rect.left = x
        CHA_rect.top = y
        if bulletc >=0:
            for i in bullet:
                if i[2]==1:
                    i[0] = i[0]+ 15
                    screen.blit(bull1, (i[0], i[1]))
                if i[2]==0:
                    i[0] = i[0]- 15
                    screen.blit(bull, (i[0], i[1]))
        enrandom = random.randint(1,100)
        if enrandom > edc:
            xy = random.randint(0,1)
            en.append([xx[xy], random.randint(1,650), xy, stagem, mhp]) #[x좌표, y좌표, 좌우결정, ]
        for it in en:
            if  it[3] == 1:
                zom1 = pygame.transform.scale(pygame.image.load('1.1.png'), (80, 83))
                zom11 = pygame.transform.scale(pygame.image.load('1.2.png'), (80, 83))
            if it[3] ==2:
                zom1 = pygame.transform.scale(pygame.image.load('2.1.png'), (80, 83))
                zom11 = pygame.transform.scale(pygame.image.load('2.2.png'), (80, 83))

            if it[3] ==3:
                zom1 = pygame.transform.scale(pygame.image.load('3.1.png'), (80, 83))
                zom11 = pygame.transform.scale(pygame.image.load('3.2.png'), (80, 83))
            if it[3] ==4:
                zom1 = pygame.transform.scale(pygame.image.load('4.1.png'), (80, 83))
                zom11 = pygame.transform.scale(pygame.image.load('4.2.png'), (80, 83))
            if it[0] == -100 or it[1]==-100:
                en.remove(it)
                
            if it[2] == 0:
                speed1= (x +it[0] )/80
                speed2 = (y - it[1] )/80
                zombi = zom11
            if it[2]==1:
                speed1= (x -it[0] )/80
                speed2 = (y - it[1] )/80
                zombi = zom1
            it[0]=it[0]+speed1
            it[1]=it[1]+speed2
            zombie_rect = zombi.get_rect()
            zombie_rect.left = it[0]
            zombie_rect.top = it[1]
            if CHA_rect.colliderect(zombie_rect):
                lkk=lkk-zd
                it[0] = -100
                it[1] = -100
                en.remove(it)
            for i in bullet:
                bull_rect = bull.get_rect()
                bull_rect.left = i[0]
                bull_rect.top = i[1]
                if bull_rect.colliderect(zombie_rect):
                    k1 = it[0]
                    k2 = it[1]
                    asxz.append([k1,k2])
##                    print(asxz)
                    bullet.remove(i)
                    it[4]=it[4]-1
                    if it[4]<=0:
                        it[0] = -100
                        it[1] = -100
                        jkk=jkk+1
            if it[0]<=-100 or it[0]>=1100 or it[1] <=-100 or it[1]>=900:
                it[0] = -100
                it[1] = -100
            screen.blit(zombi, (it[0], it[1]))
        for kk in asxz:
            screen.blit(bull2, (int(kk[0]), int(kk[1])))
            ffd_rect = bull.get_rect()
            ffd_rect.left = kk[0]
            ffd_rect.top = kk[1]
##            print(iti)int

            if CHA_rect.colliderect(ffd_rect):
                asxz.remove(kk)
                bulletc=bulletc+mhp
            
        text_title1 = myFont.render(str(bulletc), True, (0,0,0))
        screen.blit(text_title1,(10,10))
        text_title2 = myFont.render(str(lkk), True, (250,0,0))
        screen.blit(text_title2,(x+7,y-20))
        if lkk<=0:
            gameover=1
        if bulletc<=0:
            bulletc=0
        if  jkk==ghh:
            stagem = 1
            text_title2 = myFont.render(str('round2'), True, (0,0,0))
            screen.blit(text_title2,(400,10))
            mhp = 2
            ghh = 15
            edc= 97

##            bnn=2
##            zh=zh+0.5
##            edc=edc-0.5
        if  jkk==ggh:
            text_title2 = myFont.render(str('round3'), True, (0,0,0))
            screen.blit(text_title2,(400,10))
            stagem = 2
            mhp = 3
            edc= 96
##            zd=5
##            zom1 = pygame.transform.scale(pygame.image.load('2.1.png'), (80, 83))
##            zom11 = pygame.transform.scale(pygame.image.load('2.2.png'), (80, 83))
##            bnn=2
##            zh=zh-0.5
##            edc=edc-0.5
        if  jkk==ggg:
            stagem = 3
            text_title2 = myFont.render(str('round4'), True, (0,0,0))
            screen.blit(text_title2,(400,10))
            mhp = 4
            edc= 96
##            zd=10
##            zom1 = pygame.transform.scale(pygame.image.load('3.1.png'), (80, 83))
##            zom11 = pygame.transform.scale(pygame.image.load('3.2.png'), (80, 83))
##            bnn=2
##            zh=zh+0.5
##            edc=edc-1
        if  jkk==hhh:
            text_title2 = myFont.render(str('round5'), True, (0,0,0))
            screen.blit(text_title2,(400,10))
            stagem = 4
            mhp = 5
            edc= 95
##            zom1 = pygame.transform.scale(pygame.image.load('4.1.png'), (80, 83))
##            zom11 = pygame.transform.scale(pygame.image.load('4.2.png'), (80, 83))
##            bnn=2
##            zd=15
##            zh=zh+0.5
##            edc=edc-0.5
        pygame.display.flip()
    if gameover == 1:
        k=0
        ad=0
        ggh=20
        ggg=30
        hhh=40
        clock= pygame.time.Clock()
        p=0
        a=[]
        bullet = []
        en=[]
        bc = 1
        lkk=100
        jkk=0
        bnn=1
        bulletc=20
        ghh=10
        edc=97
        dfg=100
        zh=1
        asxz=[]
        xx = [0, 1000]
        screen.fill((255, 255, 255))
        text_title2 = myFont1.render(str('Do you want replay?, then press SPACE'), True, (0,0,0))
        screen.blit(text_title2,(10,300))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameover=0
                    time.sleep(3)
        pygame.display.flip()
        
pygame.quit()
