'''
Student Name: Amitva Pal
Game title: Rocket Race
Period: 6/7
Features of Game: User gets to pick what colour of rocket and is randomly decided which rocket wins
'''

import pygame, sys, random                              #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=480                                                   #Open and set window size
h=800                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode((w, h))

pygame.display.set_caption("Rocket Race")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):

greenRocket=pygame.image.load("green.png")
greenRect=greenRocket.get_rect()

blueRocket=pygame.image.load("blue.png")
blueRect=blueRocket.get_rect()

clock=pygame.time.Clock()                               # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed
#Program helper functions:

def showMessage(words,myfont,size,x,y,color,bg=None):
    font=pygame.font.SysFont(myfont,size,True,False)
    textImage=font.render(words,True,color,bg)
    textBounds=textImage.get_rect()
    textBounds.center=(x,y)
    return textImage,textBounds

def drawScreen(gameInPlay,rocketChoice):
    bg=pygame.image.load("space.png")
    surface.blit(bg,[0,0])
    surface.blit(greenRocket,greenRect)
    surface.blit(blueRocket,blueRect)
    

    if gameInPlay==False:
        winner=getWinner(rocketChoice)
        winnerText,winnerBounds=showMessage(winner, "Pompa", 30, w/2, 2.5*h/4, WHITE)
        surface.blit(winnerText,winnerBounds)
        chooseText,chooseBounds=showMessage("Choose Your Race Rocket", "Pompa", 35, w/2, h/2, WHITE)
        surface.blit(chooseText,chooseBounds)
        greenButtonText,greenButtonBounds=showMessage("Choose Green Rocket?","Pompa",20,w/4,3*h/4,WHITE,bg=GREEN)
        surface.blit(greenButtonText, greenButtonBounds)   
        blueButtonText,blueButtonBounds=showMessage("Choose Blue Rocket?","Pompa",20,3*w/4,3*h/4,WHITE,bg=BLUE)
        surface.blit(blueButtonText, blueButtonBounds)
        
def initRockets():
    greenRect.bottom=h
    blueRect.bottom=h
    greenRect.centerx=w/4
    blueRect.centerx=3*w/4

def getWinner(rocketChoice):
    if rocketChoice==None:
        return ""
    elif greenRect.top==blueRect.top:
        return "Tie"
    elif rocketChoice=="green" and greenRect.top<blueRect.top:
        return "You Win"
    elif rocketChoice=="green" and blueRect.top<greenRect.top:
        return "You Lose"
    elif rocketChoice=="blue" and blueRect.top<greenRect.top:
        return "You Win"
    elif rocketChoice=="blue" and greenRect.top<blueRect.top:
        return "You Lose"

# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    #declare local game variables here
    initRockets()
    
    gameInPlay=False
    rocketChoice=None
    
    greenButtonText,greenButtonBounds=showMessage("Choose Green Rocket?","Pompa",20,w/4,3*h/4,GREEN,bg=WHITE)
        
    blueButtonText,blueButtonBounds=showMessage("Choose Blue Rocket?","Pompa",20,3*w/4,3*h/4,BLUE,bg=WHITE)
        
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            if greenButtonBounds.collidepoint(pygame.mouse.get_pos()):
                if(event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
                    rocketChoice="green"
                    initRockets()
                    gameInPlay=True
                
            elif blueButtonBounds.collidepoint(pygame.mouse.get_pos()):
                if(event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
                    rocketChoice="blue"
                    initRockets()
                    gameInPlay=True
                    
                  
                        
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        if gameInPlay==True:
            greenRect.top-=random.randint(5,10)
            blueRect.top-=random.randint(5,10)
            
            if greenRect.top<=0 or blueRect.top<=0:
                gameInPlay=False
         
        #drawing code goes here
        drawScreen(gameInPlay,rocketChoice)
        
        clock.tick(20)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
main()                                                   #this calls the main function to run the program
