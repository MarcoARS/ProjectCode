__author__ = 'm4rco_000'

import pygame
import random
#------------------------Screen setup--------------------
pygame.init()

# This functions chooses a ramdon place from where the NPP will shoot the ball
def soccer():
    init = 170
    fin = 600
    pos = random.choice(range(init,fin))
    return pos

#
def trophy(x,y,count):
    screen.blit(spriteTrophy[count],(x,y))
    x += spriteTrophy[0].get_width()
    count = count + 1

def final():
    #pygame.display.flip()
    start = False
    while not start:
     for event in pygame.event.get():
        # Verifying if player exits the game
        if event.type == pygame.QUIT:
            start = True

        #Fill the screen with green color and with the field image
        screen.fill(fieldColor)
        screen.blit(spriteField,(0,0))

        if( npcRoundW > playerRoundW ):
            #Draw each sentence at the beginning of the game
            screen.blit(gameFont.render("Sorry, you lose!", True, (91,26,94)),(225,95))
            screen.blit(gameFont.render("You have no abilities as a goalkeeper...", True, (91,26,94)),(225,115))
            screen.blit(gameFont.render("Keep studying!", True, (91,26,94)),(225,135))
            screen.blit(gameFont.render("May the force be with you...", True, (91,26,94)),(225,155))
            screen.blit( pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/lose.png"),(275,175))

        elif( playerRoundW > npcRoundW ):
            screen.blit(gameFont.render("Congratulations, you WIN!!!", True, (91,26,94)),(235,95))
            screen.blit(gameFont.render("Maybe you can play in our team next World Cup!", True, (91,26,94)),(235,115))
            screen.blit(gameFont.render("Send us your CV to analysis!", True, (91,26,94)),(235,135))
            screen.blit(pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/win.png"),(275,175))
            screen.blit(pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/balloons.png"),(300,0))


        screen.blit(spriteTrophy[0],(45,10))
        screen.blit(spriteTrophy[1],(700,10))
        screen.blit(spriteTrophy[2],(700,450))
        screen.blit(spriteTrophy[3],(45,450))


        pygame.display.flip()

        # Catch the button to start the game
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] == True:
            start = True
    return True


# Screen Size
screenWidth = 800
screenHeight = 600
#Setup my fame window screen
screen = pygame.display.set_mode( (screenWidth,screenHeight) )

# Font used to draw the scores and round of the game
gameFont = pygame.font.SysFont(None, 30)

# Sprites
fieldColor = (59,143,72)
spriteField = pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/field.jpg")
spriteGoalKeeper = pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/goalKeeper.png")
spriteSoccerPlayer = pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/soccerPlayer.png")
spriteSoccerBall = pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/soccerBall.png")
spriteBall = pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/soccerBall.png")
spriteInitial = pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/goalKeeperImage.png")

spriteTrophy = []
spriteTrophy.append(pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/trophy.png"))
spriteTrophy.append(pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/trophy.png"))
spriteTrophy.append(pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/trophy.png"))
spriteTrophy.append(pygame.image.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/trophy.png"))
count = 0

# Background Sound
pygame.mixer.music.load("C:/Users/m4rco_000/Desktop/CofC/Second Semester/Game Programming/Project/Sprites/sounds/background.ogg")
pygame.mixer.music.play(-1)


# NPC variables
npcRadius = 45
npcX = screenWidth/2
npcY = screenHeight/3
npcPoints = 0
npcTrophyX = 50
npcTrophyY = 70
npcRoundW = 0

# Ball definitions
ballX = npcX + spriteSoccerPlayer.get_width()/4
ballY = npcY + spriteSoccerPlayer.get_height()
ballStep = 4

# Player definitions
playerColor = (239, 236, 202)
playerHeight = 40
playerWidth = 40
playerX = screenWidth/2
playerY = (screenHeight - playerHeight - 30)
playerPoints = 0
playerTrophyX = 650
playerTrophyY = 70
playerRoundW = 0

# Other definitions
maxPosition = 0
minPosition = 0
done = False
gameRounds = 1
trophyX = []
trophyX.append(380)
trophyX.append(380)
trophyX.append(380)

trophyY = []
trophyY.append(70)
trophyY.append(70)
trophyY.append(70)
trophyY.append(70)

fSentence = gameFont.render("Welcome to Button Soccer!!", True, (91,26,94))
sSentence = gameFont.render("Test all your abilities as the best goalkeeper in the world!", True,(91,26,94))
tSentence = gameFont.render("Catch the balls using the left and right arrows, but be careful!", True, (91,26,94))
ftSentence = gameFont.render("Each round the npc's shoots stronger!!", True, (91,26,94))
ffSentence = gameFont.render("That who has more trophies wins the game! Good luck my friend!", True, (91,26,94))
sfSentence = gameFont.render("May the force be with you...", True, (91,26,94))
svfSentence = gameFont.render("And do not forget to press SPACE to start!", True, (91,26,94))
start = False
# --------------------------------- Game Looping -------------------- #
while not start:
     for event in pygame.event.get():
        # Verifying if player exits the game
        if event.type == pygame.QUIT:
            start = True

        #Fill the screen with green color and with the field image
        screen.fill(fieldColor)
        screen.blit(spriteField,(0,0))

        #Draw each sentence at the beginning of the game
        screen.blit(fSentence,(265,95))
        screen.blit(sSentence,(135,125))
        screen.blit(tSentence,(115,155))
        screen.blit(ftSentence,(225,185))
        screen.blit(ffSentence,(95,215))
        screen.blit(sfSentence,(275,245))
        screen.blit(spriteInitial,(275,265))
        screen.blit(svfSentence,(185,265 + spriteInitial.get_height()))

        screen.blit(spriteTrophy[0],(45,10))
        screen.blit(spriteTrophy[1],(700,10))
        screen.blit(spriteTrophy[2],(700,450))
        screen.blit(spriteTrophy[3],(45,450))


        pygame.display.flip()

        # Catch the button to start the game
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] == True:
             start = True

while not done:
    # (1) Check and respond to inputs
    # Repeat changing for event actions like key press
    for event in pygame.event.get():
        # Verifying if player exits the game
        if event.type == pygame.QUIT:
            #Set variable to say game over
            #Will cause while loop to exit
            done = True

    # GET PLAYER'S MOVEMENTS
    keys_pressed = pygame.key.get_pressed() # get current value of key pressed
    if keys_pressed[pygame.K_LEFT] == True:
        playerX = playerX- 10 # moving goalKeeper

        # Left limit of the screen
        if(playerX <= 0):
            playerX = 0

    if keys_pressed[pygame.K_RIGHT] == True: #if left arrow key is pressed
        playerX = playerX + 10

        # Right limit of the screen
        if(playerX >= screenWidth):
            playerX = screenWidth - playerWidth

    # Shoot the ball
    ballY += ballStep
    if(ballY > 580): # Verification if the npc goal!
        npcPoints += 1

        npcX = soccer() # Call the random movement for npc
        ballY = npcY + spriteSoccerPlayer.get_height() # ball returns to npc
        ballX = npcX + spriteSoccerPlayer.get_width()/4 # ball returns to npc

    if (ballY >= (playerY + spriteGoalKeeper.get_height()/3) and
            (ballX >= playerX - spriteGoalKeeper.get_width()/2) and
                ballX <= (playerX + spriteGoalKeeper.get_width())):
        playerPoints += 1

        npcX = soccer() # Call the random movement for npc
        ballY = npcY + spriteSoccerPlayer.get_height() # ball returns to npc
        ballX = npcX + spriteSoccerPlayer.get_width()/4 # ball returns to npc


    if (npcPoints >= 5 or playerPoints >= 10):
        if(npcPoints >= 5 ):
            trophyX[count] = npcTrophyX
            trophyY[count] = npcTrophyY
            count += 1
            npcRoundW += 1
            npcTrophyX += spriteTrophy[0].get_width()
        elif(playerPoints >= 10 ):
            trophyX[count] = playerTrophyX
            trophyY[count] = playerTrophyY
            count += 1
            playerRoundW += 1
            playerTrophyX += spriteTrophy[0].get_width()
        ballStep += 1
        gameRounds += 1
        npcPoints = 0
        playerPoints = 0



    screen.fill(fieldColor)
    screen.blit(spriteField,(0,0))

    # Draw soccer player
    screen.blit(spriteSoccerPlayer,(npcX,npcY))

    # Draw soccer ball
    screen.blit(spriteSoccerBall,(ballX,ballY))

    # Draw GoalKeeper
    screen.blit(spriteGoalKeeper,(playerX,playerY))

    playerScore = gameFont.render("Player score: "+str(playerPoints), True, (0,0,0))
    npcScore = gameFont.render("NPC score: "+str(npcPoints), True, (0,0,0))
    round = gameFont.render("Round: "+str(gameRounds), True, (0,0,0))
    screen.blit(npcScore,(50,25))
    screen.blit(playerScore,(610,25))
    screen.blit(round,(350,25))


    screen.blit(spriteTrophy[0],(trophyX[0],trophyY[0]))
    screen.blit(spriteTrophy[1],(trophyX[1],trophyY[1]))
    screen.blit(spriteTrophy[2],(trophyX[2],trophyY[2]))



    # Refresh screen display.
    pygame.display.flip()
    if(gameRounds > 3):
            done = final()
