from pygame import *
from random import *
import math

width,height=1200,800
screen=display.set_mode((width,height))
WHITE=(255,255,255)
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)

#initializing fonts
font.init()
comicFont=font.SysFont("Comic Sans MS",15)


#initializing variables
xpos=[]
ypos=[]
xspeed=0
yspeed=0
gravity=0
projectiley=0

count=0

enemies = []

charging = False

shoot = False

dead= False

setting = 1 #1: main menu 2: play 3: shop
shopSetting = 1 # Only when in shop 1: weapons 2: armor 3: special 4: stats

running=True

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = mouse.get_pos()
            screenshot = screen.copy()
            if evt.button == 1:
                click = True
            if evt.button == 3:
                right_click = True
            if evt.button == 4 and size <= 30:
                size += 1
            if evt.button == 5 and size >=1:
                size -= 1
            if evt.type==MOUSEBUTTONUP:
                screen.blit(screenCap,(0,0))
                click=False

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

        
#Main Menu-----------------------------------------------------------------------------

    if setting == 1:

        play=Rect(900,300,200,60)
        shop=Rect(900,400,200,60)

        if mb[0] == 1 and play.collidepoint(mx,my):
            setting = 2

        if mb[0] == 1 and shop.collidepoint(mx,my):
            setting = 3
        #background
        background=image.load("images/Background.png")
        screen.blit(background,(0,0))

        draw.rect(screen,BLACK,(900,300,200,60))
        draw.rect(screen,BLACK,(900,400,200,60))

        if play.collidepoint(mx,my):
            draw.rect(screen,WHITE,(900,300,200,60),5)
        if shop.collidepoint(mx,my):
            draw.rect(screen,WHITE,(900,400,200,60),5)
        
        #Texts
        comicFont=font.SysFont("Comic Sans MS",70)
        title=comicFont.render("Katsura Kastle Defense",True,BLACK)
        screen.blit(title,(300,100))
        comicFont=font.SysFont("Comic Sans MS",25)
        playButton=comicFont.render("PLAY",True,WHITE)
        screen.blit(playButton,(920,310))
        shopButton=comicFont.render("SHOP",True,WHITE)
        screen.blit(shopButton,(920,410))
                
#Play-----------------------------------------------------------------------------------

    if setting == 2:
        #background
        draw.rect(screen,BLACK,(0,0,1200,80))
        kastle=image.load("images/Castle.jpg")
        screen.blit(kastle,(0,80))

        #info
        score=comicFont.render("SCORE:",True,WHITE)
        screen.blit(score,(100,30))

        #Game--------------------------------------------------

        #player
        playerBody=Rect(48,710,22,25)
        playerFeet=Rect(50,740,18,30)
        draw.circle(screen,BLACK,(59,700),12)
        draw.rect(screen,BLACK,(48,710,22,25))
        draw.rect(screen,BLACK,(50,735,18,30))
        

        #Shooting
        
        if mb[0] == 1 and shoot == False:
            draw.line(screen,BLACK,(sx,sy),(mx,my),5)
            shoot = True
            
        if shoot == True and mb[0] == 0 and sx!=mx and sy!=my:
            if len(xpos)==0:
                xpos.append(mx)
                ypos.append(my)
            h=abs(ypos[0]-sy)
            l=sx-xpos[0]
            gravity+=0.6
            yspeed=yspeed+h/20
            xspeed=xspeed+l/30
            projectiley=int(700-yspeed+gravity**2)
            draw.circle(screen,BLACK,(int(xspeed+50),projectiley),5)
        if projectiley>800:
            xspeed=0
            yspeed=0
            gravity=0
            projectiley=0
            xpos=[]
            ypos=[]
            shoot=False
        print(shoot)
                

        


            
            
        
        
        #Enemies
        if len(enemies)<5:
            hello = (randint(200,1000),randint(100,700))
            enemies.append(hello)
        for i in range(len(enemies)):
            draw.circle(screen,WHITE,enemies[i],50)
        
        
        #-------------------------------------------------------
        if mb[2] == 1:
            dead = True
        if dead == True:
            setting = 1
            dead = False
            
#Shop------------------------------------------------------------------------------

    if setting == 3:

        weaponItems = ["bow","samurai sword","a","b"]
        armorItems = []
        specialAbilityItems = []
        statsItems = []
        
        back=Rect(0,0,100,50)
        weapons=Rect(205,140,190,50)
        armor=Rect(405,140,190,50)
        special=Rect(605,140,190,50)
        stats=Rect(805,140,190,50)
        up=Rect(900,260,30,30)
        down=Rect(900,610,30,30)
        selectionBar=Rect(900,300-count,30,300//len(weaponItems))
        border=Rect(250,250,700,400)
        bigBorder=Rect(200,200,800,500)

        lis = [weapons,armor,special,stats]

        if mb[0]==1 and weapons.collidepoint(mx,my):
            shopSetting = 1
            draw.rect(screen,BLACK,(250,250,700,400))
        
        if mb[0]==1 and armor.collidepoint(mx,my):
            shopSetting = 2
            draw.rect(screen,BLACK,(250,250,700,400))
            
        if mb[0]==1 and special.collidepoint(mx,my):
            shopSetting = 3
            draw.rect(screen,BLACK,(250,250,700,400))
            
        if mb[0]==1 and stats.collidepoint(mx,my):
            shopSetting = 4
            draw.rect(screen,BLACK,(250,250,700,400))

        if shopSetting == 1:#Weapons section

            #background
            background2 = image.load("images/Background2.png")
            screen.blit(background2,(0,0))

            #Boxes
            draw.rect(screen,GREEN,(0,0,100,50))
            for i in range(4):
                draw.rect(screen,GREEN,((i+1)*200+5,140,190,50))
            draw.rect(screen,GREEN,(200,200,800,500))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(205,140,190,50),5)

            #Items
            
            draw.rect(screen,WHITE,(900,300-count,30,300//len(weaponItems)))
            
            draw.rect(screen,WHITE,(900,260,30,30))
            draw.rect(screen,WHITE,(900,610,30,30))

            if mb[0] == 1 and up.collidepoint(mx,my) and selectionBar.collidepoint(910,300)==False:
                selectionBar=Rect(900,300-count,30,300//len(weaponItems))
                count+=5
            if mb[0] == 1 and down.collidepoint(mx,my) and selectionBar.collidepoint(910,600)==False:
                selectionBar=Rect(900,300+count,30,300//len(weaponItems))
                count-=5

            for i in range(3):
                draw.rect(screen,WHITE,(300,275+120*i,500,100))
                
            
        if shopSetting == 2:#Armor section

            background3 = image.load("images/Background3.png")
            screen.blit(background3,(0,0))
            draw.rect(screen,GREEN,(0,0,100,50))
            for i in range(4):
                draw.rect(screen,GREEN,((i+1)*200+5,140,190,50))
            draw.rect(screen,GREEN,(200,200,800,500))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(405,140,190,50),5)
            
        if shopSetting == 3:#Special abilities section
            background4 = image.load("images/Background4.jpg")
            screen.blit(background4,(0,0))
            draw.rect(screen,GREEN,(0,0,100,50))
            for i in range(4):
                draw.rect(screen,GREEN,((i+1)*200+5,140,190,50))
            draw.rect(screen,GREEN,(200,200,800,500))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(605,140,190,50),5)
            
        if shopSetting == 4:#stats section
            background5 = image.load("images/Background5.jpg")
            screen.blit(background5,(0,0))
            draw.rect(screen,GREEN,(0,0,100,50))
            for i in range(4):
                draw.rect(screen,GREEN,((i+1)*200+5,140,190,50))
            draw.rect(screen,GREEN,(200,200,800,500))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(805,140,190,50),5)

        #Hovering mouse over stuff
        for i in range(4):
            if lis[i].collidepoint(mx,my):
                draw.rect(screen,BLACK,(i*200+205,140,190,50),5)
        if back.collidepoint(mx,my):
            draw.rect(screen,BLACK,(0,0,100,50))

        #Displaying Text
        backButton=comicFont.render("Back",True,WHITE)
        screen.blit(backButton,(15,12))

        backButton=comicFont.render("Weapons",True,BLACK)
        screen.blit(backButton,(225,145))
        backButton=comicFont.render("Armor",True,BLACK)
        screen.blit(backButton,(425,145))
        backButton=comicFont.render("Special",True,BLACK)
        screen.blit(backButton,(625,145))
        backButton=comicFont.render("Stats",True,BLACK)
        screen.blit(backButton,(825,145))
            
        if mb[0] == 1 and back.collidepoint(mx,my):
            setting = 1
        
   
    display.flip()
            
quit()

