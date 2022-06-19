#Name: Breakout Arcade Game
#Programmer: Gloria Wang & Mark Chen
#Date: May 10, 2022
#Description: This game allows a user to play a version of Atari's Breakout Arcade Game

displayScreen = 0


def setup():
    global logo, life
    size(1000, 600)
    background(0)
    textAlign(CENTER)
    logo = loadImage('breakoutlogo.gif')
    life = loadImage('lifeicon1.png')
    

def draw():
    if displayScreen == 0:
        startScreen()


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
    text("and music will be in the top right. ", 500, 400)
    
    #Play button
    strokeWeight(10)
    stroke(150, 200, 120)
    fill(100, 150, 170)
    rect(400, 470, 200, 50)
    textSize(20)
    fill(255)
    text("PRESS TO START", 500, 502)
