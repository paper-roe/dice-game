import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

icon = pygame.image.load('apple2.png')
pygame.display.set_icon(icon)

snakeimg = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple2.png')

clock = pygame.time.Clock()
FPS = 15

direction = 'right'

block_size = 20
appleThickness = 30

smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)

def pause():
    paused = True
    
    message_to_screen('Paused',
                      black,
                      -100,
                      'large')
    message_to_screen('Press C to continue or Q to quit',
                      black,
                      25)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallfont.render('Score: ' + str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randAppleGen():
    randAppleX = random.randrange(0, display_width-block_size, appleThickness)
    randAppleY = random.randrange(0, display_height-block_size, appleThickness)

    return randAppleX, randAppleY

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
        gameDisplay.fill(white)
        
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          'large')
        
        message_to_screen('The objective of the game is to eat red apples',
                          black,
                          -30)
        
        message_to_screen('The more apples eat, the longer you get',
                          black,
                          10)
        
        message_to_screen('If you run into yourself, or the edges, you die!',
                          black,
                          50)

        message_to_screen('Press C to play, P to pause or Q to quit.',
                          black,
                          180)

        pygame.display.update()
        clock.tick(5)

def snake(block_size, snakeList):
    if direction == 'right':
        head = pygame.transform.rotate(snakeimg, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snakeimg, 90)
    if direction == 'up':
        head = snakeimg
    if direction == 'down':
        head = pygame.transform.rotate(snakeimg, 180)
    
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1], block_size,block_size])

def text_objects(text, colour, size='small'):
    if size == 'small':
        textSurface = smallfont.render(text, True, colour)
    elif size == 'medium':
        textSurface = medfont.render(text, True, colour)
    elif size == 'large':
        textSurface = largefont.render(text, True, colour)
    
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, colour, y_displace=0, size='small'):
    textSurf, textRect = text_objects(msg, colour, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def game_loop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = random.randrange(0, display_width-block_size, appleThickness)
    randAppleY = random.randrange(0, display_height-block_size, appleThickness)

    while not gameExit:

        if gameOver == True:
            message_to_screen('Game Over',
                              red,
                              -50,
                              'large')
            message_to_screen('Press C to play again or Q to quit',
                              black,
                              50,
                              'medium')
            pygame.display.update()

        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'right':
                    lead_y_change = 0
                    lead_x_change = -block_size
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    lead_y_change = 0
                    lead_x_change = block_size
                    direction = 'right'
                elif event.key == pygame.K_UP and direction != 'down':
                    lead_x_change = 0
                    lead_y_change = -block_size
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    lead_x_change = 0
                    lead_y_change = block_size
                    direction = 'down'
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
                
        gameDisplay.fill(white)

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness,appleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for segment in snakeList[:-1]:
            if segment == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)

        score(snakeLength-1)

        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()
    
game_intro()
game_loop()