add_library('minim')

displayScreen = 0
gameWon = False
lives = 3
score = 0
ballX = random(1000)
ballY = 550
ballSpeedX = -3
ballSpeedY = -3
bricks = [ [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True] ]
brickX = 0
brickY = 0
brickColour = 0
brickCounter = 0
musicPlay = True
gamePause = False
level = 1
time = 0


def setup():
    global logo, life, start, music, song, replay, play, pause, win, lose
    size(1000, 600)
    background(0)
    textAlign(CENTER)
    logo = loadImage('breakoutlogo.gif')
    life = loadImage('lifeicon1.png')
    start = loadImage('start1.png')
    music = loadImage('music1.png')
    replay = loadImage('playagain1.png')
    play = loadImage('play1.png')
    pause = loadImage('pause1.png')
    win = loadImage('win.jpg')
    lose = loadImage('gameover1.jpg')
    
    minim = Minim(this)
    song = minim.loadFile("Song.mp3")
    song.loop()


def draw():
    background(0)    
    if displayScreen == 0:
        startScreen()    
    elif displayScreen == 2:
        endScreen()
    elif displayScreen == 1:
        gameScreen()


def startScreen():
    #Title
    image(logo, (width - logo.width) / 2, 50)
    
    #Instructions
    fill(255)
    textSize(30)
    text("Instructions & Rules", 500, 250)
    
    fill(255, 0, 0)
    textSize(15)
    text("A brick wall is at the top section of the screen, use the mouse to", 500, 300)
    text("control the paddle and hit the ball upwards. The ball will eliminate", 500, 320)
    text("the blocks and when all the blocks are gone, YOU WIN. You have 3", 500, 340)
    text("lives to do so. You lose a life if the ball goes past the paddle. Once,", 500, 360)
    text("all 3 lives are gone, YOU LOSE. The game info will be in the top left", 500, 380)
    text("and music and play/pause button will be in the top right. ", 500, 400)
    
    #Play button
    image(start, 425, 450)
    
    
def gameScreen():
    global ballX, ballY, ballSpeedX, ballSpeedY, lives, mouseX, displayScreen, gameWon, paddleLeft, level, bricks, musicPlay, gamePause, time
    
    #Timer
    time += 1
    timer()
        
    #Settings bar
    fill(160)
    rect(0, 0, 1000, 50)
    
    #Lives indicator
    livesCount()
        
    #Music play/pause
    image(music, 955, 10)
    
    #Play or pause the game
    if gamePause == True:
        image(play, 915, 10)
    elif gamePause == False:
        image(pause, 915, 10)
    
    #Score indicator
    textAlign(LEFT)
    msg = "SCORE: " + str(score)
    textSize(30)
    fill(0)
    text(msg, 140, 35)
  
    brick()
  
    #Ball
    if gamePause == False:
        ballX += ballSpeedX
        ballY += ballSpeedY
    if gamePause == True:
        ballX += 0
        ballY += 0   
    fill(120)
    ball = ellipse(ballX, ballY, 18, 18)
    
    if ballX + 9 >= width:
        ballSpeedX = -ballSpeedX
        ballX = width - 9
    elif ballX - 9 <= 0:
        ballSpeedX = -ballSpeedX
        ballX = 9
    if ballY + 9 >= height:
        ballY = height - 9
        ballSpeedX = 0
        lives -= 1 
        ballSpeedX = -3
        ballSpeedY = -3
        delay(1000) #Gives user time to prepare for next play
    elif ballY - 9 <= 50:
        ballSpeedY = -ballSpeedY
        ballY = 59
    
    fill(0, 0, 255)
    paddleLeft = mouseX - 80
    rect(paddleLeft, 550, 160, 20)
    if mouseX < 0:
        paddleLeft = -80
    if mouseX > 1000: 
        paddleLeft = 920
    
    if ballY + 9 >= 550:
        if ballX >= paddleLeft and ballX < paddleLeft + 60:
            ballSpeedY = -ballSpeedY
            ballY = 541
            if ballSpeedX > 0:
                ballSpeedX = -ballSpeedX
        if ballX >= paddleLeft + 100 and ballX <= paddleLeft + 160:
            ballSpeedY = -ballSpeedY
            ballSpeedX = -ballSpeedX
            ballY = 541
            if ballSpeedX < 0:
                ballSpeedX = -ballSpeedX
        if ballX >= paddleLeft + 60 and ballX < paddleLeft + 80: #ntbf
            ballSpeedY = -ballSpeedY
            ballSpeedX = ballSpeedX / 2
            ballY = 541
            if ballSpeedX > 0:
                ballSpeedX = -ballSpeedX / 2
            time += 1
        if ballX >= paddleLeft + 80 and ballX < paddleLeft + 100: #ntbf // goes straight up and stays like that
            ballSpeedY = -ballSpeedY
            ballSpeedX = -ballSpeedX / 2
            ballY = 541
            if ballSpeedX < 0:
                ballSpeedX = -ballSpeedX / 2  
            time += 1
              
                
    if bricks == [ [False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False] ]:
        displayScreen = 2
        gameWon = True


    #Play or pause the game images
    if gamePause == True:
        image(play, 915, 10)
    if gamePause == False:
        image(pause, 915, 10)
        
    print("ballSpeedX is " + str(ballSpeedX) + "ballSpeedY is " + str(ballSpeedY))

                    
def endScreen():
    
    #Score box
    textAlign(CENTER)
    textSize(50)
    fill(255)
    text("LEVEL: " + str(level) + " SCORE: " + str(score), 500, 280)
    
    image(replay, 397, 450)
    
    if gameWon == True:
        image(win, 288, 100)
    if gameWon == False:
        image(lose, 287, 100)

def brick():
    global ballSpeedX, ballSpeedY, score, level
    for i in range(5):
        for j in range(9):
            if i == 0:
                fill(255, 0, 0)
                points = 50
            if i == 1:
                fill(255, 140, 0)
                points = 40
            if i == 2:
                fill(255, 255, 0)
                points = 30
            if i == 3:
                fill(0, 255, 0)
                points = 20
            if i == 4:
                fill(0, 0, 255)
                points = 10
                
            if bricks[i][j] == True:
                rect(j * 100 + (j + 1) * 10, i * 40 + (i + 1) * 10 + level * 50, 100, 40)

                #Interaction with blocks // ntbf
                if ballX + 9 >= j * 100 + (j + 1) * 10 and ballX - 9 <= j * 100 + (j + 1) * 10 and ballY + 9 >= i * 40 + (i + 1) * 10 + level * 50 and ballY - 9 <= i * 40 + (i + 1) * 10 + level * 50 + 40:
                    ballSpeedX = -ballSpeedX
                    bricks[i][j] = False
                    score += points
                if ballX - 9 <= j * 100 + (j + 1) * 10 + 100 and ballX + 9 >= j * 100 + (j + 1) * 10 + 100 and ballY + 9 >= i * 40 + (i + 1) * 10 + level * 50 and ballY - 9 <= i * 40 + (i + 1) * 10 + level * 50 + 40:
                    ballSpeedX = -ballSpeedX
                    bricks[i][j] = False
                    score += points
                if ballY + 9 >= i * 40 + (i + 1) * 10 + level * 50 and ballY - 9 <= i * 40 + (i + 1) * 10 + level * 50 and ballX + 9 >= j * 100 + (j + 1) * 10 and ballX - 9 <= j * 100 + (j + 1) * 10 + 100:
                    ballSpeedY = -ballSpeedY
                    bricks[i][j] = False
                    score += points
                if ballY - 9 <= i * 40 + (i + 1) * 10 + level * 50 + 40 and ballY + 9 >= i * 40 + (i + 1) * 10 + level * 50 + 40 and ballX + 9 >= j * 100 + (j + 1) * 10 and ballX - 9 <= j * 100 + (j + 1) * 10 + 100:
                    ballSpeedY = -ballSpeedY
                    bricks[i][j] = False
                    score += points
                    
            if ballSpeedX == 0:
                ballSpeedX = ballSpeedX + 2
                time = 0
                    
            if level == 2:
                ballSpeedX = ballSpeedX * 1.5
                ballSpeedY = ballSpeedY * 1.5
            

def mousePressed():
    global displayScreen, bricks, lives, score, song, musicPlay, gamePause, time, level, ballX, ballY, ballSpeedX, ballSpeedY

    if displayScreen == 0 and mouseX >= 425 and mouseX <= 575 and mouseY >= 450 and mouseY <= 525:
        displayScreen = 1
        
    if displayScreen == 2 and mouseX >= 397 and mouseX <= 603 and mouseY >= 450 and mouseY <= 525:
        displayScreen = 0
        for i in range(5):
            for j in range(9):
                score = 0
                lives = 3
                bricks[i][j] = True
                level = 1
                ballX = random(1000)
                ballY = 550
                ballSpeedX = -3
                ballSpeedY = -3
    
    #Play or pause the music by pressing on the music icon
    if mouseX >= 955 and mouseY <= 40:
        if musicPlay == True:
            song.pause()            
            musicPlay = False
        else:
            song.play()
            musicPlay = True

    #Play or pause the game by pressing on an icon. Icon changes depending on gamePause bool      
    if mouseX >= 915 and mouseX < 955 and mouseY <= 40:
        if gamePause == True:
            gamePause = False
            time += 1
        else:
            gamePause = True
            time += 0
            
def timer():
    global time, ballSpeedX, ballSpeedY
    if time == 900:
        ballSpeedX = ballSpeedX * 2
        ballSpeedY = ballSpeedY * 2

def livesCount(): 
    global lives, displayScreen, gameWon
    if lives == 3:
        image(life, 15, 10)
        image(life, 55, 10)
        image(life, 95, 10)
    if lives == 2:
        image(life, 15, 10)
        image(life, 55, 10)     
    if lives == 1:
        image(life, 15, 10)    
    if lives == 0:
        displayScreen = 2
        gameWon = False
