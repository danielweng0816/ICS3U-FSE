from pygame import *
from random import *
from math import *

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
cointext=comicFont.render("Coins:",True,WHITE)


#initializing variables
coins=0
score=0

xpos=[]
ypos=[]
xspeed=0
yspeed=0
gravity=0
projectilex=0
projectiley=0
def dist(a,b,c,d):
    return ((c-a)**2+(d-b)**2)**0.5
hit = False
release = False

health=100

projectiles = []

count=0

enemiesx = []
enemiesy = []

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
            if evt.button == 4:
                up=True
            if evt.button == 5:
                down=True
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
        cointext=comicFont.render("Coins:",True,BLACK)
        screen.blit(cointext,(900,30))
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
        scoretext=comicFont.render("SCORE:",True,WHITE)
        currentscore=comicFont.render(str(score),True,WHITE)
        screen.blit(scoretext,(100,30))
        screen.blit(currentscore,(200,30))
        cointext=comicFont.render("Coins:",True,WHITE)
        screen.blit(cointext,(900,30))

        #Game--------------------------------------------------

        #player
        playerBody=Rect(48,710,22,25)
        playerFeet=Rect(50,740,18,30)
        draw.circle(screen,BLACK,(59,700),12)
        draw.rect(screen,BLACK,(48,710,22,25))
        draw.rect(screen,BLACK,(50,735,18,30))
        
        #weapons
        weapon="bow"
        if weapon=="bow":
            
        #Shooting
            if mb[0] == 1 and shoot == False:
                draw.line(screen,BLACK,(sx,sy),(mx,my),5)
                pull=True
            if pull==True and mb[0] == 0:
                release=True
            if pull==True and release==True:
                shoot=True
                pull=False
            
            if shoot == True and sx!=mx and sy!=my:
                if len(xpos)<2:
                    xpos.append(mx)
                    ypos.append(my)
                h=abs(ypos[0]-sy)
                l=sx-xpos[0]
                gravity+=0.65
                yspeed=yspeed+h/20
                xspeed=xspeed+l/30


            projectilex=int(xspeed)+50
            projectiley=int(700-yspeed+gravity**2)
            draw.circle(screen,BLACK,(projectilex,projectiley),5)

            if projectiley>800:
                xspeed=0
                yspeed=0
                gravity=0
                projectiley=0
                xpos=[]
                ypos=[]
                shoot=False
                release=False

        if weapon=="hello":
            #shooting
            if mb[0] == 1:
                speed=100
                xpos=mx
                ypos=my
                distx=abs(xpos-50)
                disty=abs(700-ypos)
                dist=(distx**2+disty**2)**0.5
                xspeed=distx/dist*speed
                yspeed=disty/dist*speed
            projectilex=int(xspeed)+50
            projectiley=int(700-yspeed)
            draw.circle(screen,GREEN,(int(projectilex),int(projectiley)),5)

            if projectiley>800 or projectiley<0 or projectilex>1000 or projectilex<0:
                xspeed=0
                yspeed=0
                gravity=0
                xpos=[]
                ypos=[]
                shoot=False

            
            
                
            
            


        #Health
        draw.rect(screen,RED,(300,50,health,15))

        if playerBody.collidepoint(mx,my) or playerFeet.collidepoint(mx,my):
            health-=1

        if health==0:
            print("Game Over")
            dead=True
        
                

        


            
            
        
        
        #Enemies
        if len(enemiesx)<5:
            enemiesx.append(randint(200,1000))
            enemiesy.append(randint(100,700))
        for i in range(len(enemiesx)):
            if hit == False:
                draw.circle(screen,WHITE,(enemiesx[i],enemiesy[i]),50)
            if dist(projectilex,projectiley,enemiesx[i],enemiesy[i])<55:
                hit=True
            if hit == True:
                coins+=1
                score+=1
                enemiesx.remove(enemiesx[i])
                enemiesy.remove(enemiesy[i])
                hit=False
                break

        #Enemies shooting
        
        
        
        #-------------------------------------------------------
        if dead == True:
            screen.fill(0)
            backToMenu=Rect(400,400,400,80)
            draw.rect(screen,GREEN,(400,400,400,80))
            if mb[0] == 1 and backToMenu.collidepoint(mx,my):
                setting = 1
                dead = False
                score=0
                health = 100
            
#Shop------------------------------------------------------------------------------

    if setting == 3:

        weaponItems = ["bow","a","b","c"]
        armorItems = ["a","b","c","d"]
        specialAbilityItems = ["a","b","c","d"]
        statsItems = ["a","b","c","d"]
        
        back=Rect(0,0,100,50)
        weapons=Rect(205,140,190,50)
        armor=Rect(405,140,190,50)
        special=Rect(605,140,190,50)
        stats=Rect(805,140,190,50)
        up=Rect(900,260,30,30)
        down=Rect(900,610,30,30)
        border=Rect(250,250,700,400)
        bigBorder=Rect(200,200,800,500)
    

        lis = [weapons,armor,special,stats]

        if mb[0]==1 and weapons.collidepoint(mx,my):
            count=0
            shopSetting = 1
            draw.rect(screen,BLACK,(250,250,700,400))
        
        elif mb[0]==1 and armor.collidepoint(mx,my):
            count=0
            shopSetting = 2
            draw.rect(screen,BLACK,(250,250,700,400))
            
        elif mb[0]==1 and special.collidepoint(mx,my):
            count=0
            shopSetting = 3
            draw.rect(screen,BLACK,(250,250,700,400))
            
        elif mb[0]==1 and stats.collidepoint(mx,my):
            count=0
            shopSetting = 4
            draw.rect(screen,BLACK,(250,250,700,400))

        if shopSetting == 1:#Weapons section
            selectionBar=Rect(900,300-count,30,300//len(weaponItems))

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

            selectionBar=Rect(900,300-count,30,300//len(armorItems))

            background3 = image.load("images/Background3.png")
            screen.blit(background3,(0,0))
            draw.rect(screen,GREEN,(0,0,100,50))
            for i in range(4):
                draw.rect(screen,GREEN,((i+1)*200+5,140,190,50))
            draw.rect(screen,GREEN,(200,200,800,500))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(405,140,190,50),5)

            draw.rect(screen,WHITE,(900,300-count,30,300//len(armorItems)))
            
            draw.rect(screen,WHITE,(900,260,30,30))
            draw.rect(screen,WHITE,(900,610,30,30))

            if mb[0] == 1 and up.collidepoint(mx,my) and selectionBar.collidepoint(910,300)==False:
                selectionBar=Rect(900,300-count,30,300//len(armorItems))
                count+=5
            if mb[0] == 1 and down.collidepoint(mx,my) and selectionBar.collidepoint(910,600)==False:
                selectionBar=Rect(900,300+count,30,300//len(armorItems))
                count-=5

            for i in range(3):
                draw.rect(screen,WHITE,(300,275+120*i,500,100))
            
        if shopSetting == 3:#Special abilities section

            selectionBar=Rect(900,300-count,30,300//len(specialAbilityItems))
            
            background4 = image.load("images/Background4.jpg")
            screen.blit(background4,(0,0))
            draw.rect(screen,GREEN,(0,0,100,50))
            for i in range(4):
                draw.rect(screen,GREEN,((i+1)*200+5,140,190,50))
            draw.rect(screen,GREEN,(200,200,800,500))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(605,140,190,50),5)

            draw.rect(screen,WHITE,(900,300-count,30,300//len(specialAbilityItems)))
            
            draw.rect(screen,WHITE,(900,260,30,30))
            draw.rect(screen,WHITE,(900,610,30,30))

            if mb[0] == 1 and up.collidepoint(mx,my) and selectionBar.collidepoint(910,300)==False:
                selectionBar=Rect(900,300-count,30,300//len(specialAbilityItems))
                count+=5
            if mb[0] == 1 and down.collidepoint(mx,my) and selectionBar.collidepoint(910,600)==False:
                selectionBar=Rect(900,300+count,30,300//len(specialAbilityItems))
                count-=5

            for i in range(3):
                draw.rect(screen,WHITE,(300,275+120*i,500,100))
            
        if shopSetting == 4:#stats section

            selectionBar=Rect(900,300-count,30,300//len(statsItems))
            
            background5 = image.load("images/Background5.jpg")
            screen.blit(background5,(0,0))
            draw.rect(screen,GREEN,(0,0,100,50))
            for i in range(4):
                draw.rect(screen,GREEN,((i+1)*200+5,140,190,50))
            draw.rect(screen,GREEN,(200,200,800,500))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(250,250,700,400))
            draw.rect(screen,BLACK,(805,140,190,50),5)

            draw.rect(screen,WHITE,(900,300-count,30,300//len(statsItems)))
            
            draw.rect(screen,WHITE,(900,260,30,30))
            draw.rect(screen,WHITE,(900,610,30,30))

            if mb[0] == 1 and up.collidepoint(mx,my) and selectionBar.collidepoint(910,300)==False:
                selectionBar=Rect(900,300-count,30,300//len(statsItems))
                count+=5
            if mb[0] == 1 and down.collidepoint(mx,my) and selectionBar.collidepoint(910,600)==False:
                selectionBar=Rect(900,300+count,30,300//len(statsItems))
                count-=5

            for i in range(3):
                draw.rect(screen,WHITE,(300,275+120*i,500,100))

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
