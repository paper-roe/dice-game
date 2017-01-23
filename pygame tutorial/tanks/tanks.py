import pygame
import time
import random

pygame.init()

# colours
white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (0,155,0)
light_green = (0,255,0)

# clock
clock = pygame.time.Clock()
FPS = 15

# display
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')

# tank setup
tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

# fonts
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
        
        message_to_screen("Welcome to Tanks",
                          green,
                          -100,
                          'large')
        
        message_to_screen('The objective is to shoot and destroy',
                          black,
                          -30)
        
        message_to_screen('the enemy tank before they destroy you.',
                          black,
                          10)
        
        message_to_screen('The more enemies you destroy the harder they get',
                          black,
                          70)

        button('play', 150,500, 100,50, green, light_green, action='play')
        button('controls', 350,500, 100,50, yellow, light_yellow, \
               action='controls')
        button('quit', 550,500, 100, 50, red, light_red, action='quit')

        pygame.display.update()
        clock.tick(15)


def text_objects(text, colour, size='small'):
    if size == 'small':
        textSurface = smallfont.render(text, True, colour)
    elif size == 'medium':
        textSurface = medfont.render(text, True, colour)
    elif size == 'large':
        textSurface = largefont.render(text, True, colour)
    
    return textSurface, textSurface.get_rect()


def text_to_button(msg, colour, buttonx, buttony, buttonw, buttonh, \
                   fontSize='small'):
    textSurf, textRect = text_objects(msg, colour, fontSize)
    textRect.center = (buttonx+(buttonw)/2), (buttony+(buttonh)/2)
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, colour, y_displace=0, size='small'):
    textSurf, textRect = text_objects(msg, colour, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    
    gameDisplay.blit(textSurf, textRect)


def barrier(xlocation,randomHeight,barrier_width):
    pygame.draw.rect(gameDisplay, black, \
                     (xlocation,display_height-randomHeight, barrier_width,randomHeight))


def tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x-27,y),
                       (x-26,y-5),
                       (x-25,y-8),
                       (x-23,y-12),
                       (x-20,y-14),
                       (x-18,y-15),
                       (x-15,y-17),
                       (x-13,y-19),
                       (x-11,y-21)
                       ]
    
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight,y,tankWidth,tankHeight))

    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], \
                     turretWidth)
    
    startX = 15
    for i in range(7):
        pygame.draw.circle(gameDisplay, black, (x-startX,y+20), wheelWidth)
        startX -= 5


def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        
        message_to_screen("Controls",
                          green,
                          -100,
                          'large')
        
        message_to_screen('Fire: Spacebar',
                          black,
                          -30)
        
        message_to_screen('Move Turret: Up and Down arrows',
                          black,
                          10)
        
        message_to_screen('Move Tank: Left and Right arrows',
                          black,
                          50)

        message_to_screen('Pause: P',
                          black,
                          90)

        button('play', 150,500, 100,50, green, light_green, action='play')
        button('main', 350,500, 100,50, yellow, light_yellow, action='main')
        button('quit', 550,500, 100, 50, red, light_red, action='quit')

        pygame.display.update()
        clock.tick(15)


def button(text, x, y, w, h, inactive_colour, active_colour, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y + h > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_colour, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            elif action == 'controls':
                game_controls()
            elif action == 'play':
                game_loop()
            elif action == 'main':
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, inactive_colour, ((x,y), (w,h)))

    text_to_button(text, black, x, y, w, h)


def game_loop():
    gameExit = False
    gameOver = False

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0

    currentTurPos = 0
    changeTur = 0

    # barrier
    xlocation = (display_width/2)+ \
                (random.randint(-0.2*display_width,0.2*display_width))
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)
    barrier_width = 50
    
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
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_UP:
                    changeTur = 1
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                elif event.key == pygame.K_p:
                    pause()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    tankMove = 0
                elif event.key == pygame.K_RIGHT:
                    tankMove = 0
                elif event.key == pygame.K_UP:
                    changeTur = 0
                elif event.key == pygame.K_DOWN:
                    changeTur = 0

        gameDisplay.fill(white)

        # player
        mainTankX += tankMove
        currentTurPos += changeTur
        if currentTurPos < 0:
            currentTurPos = 0
        elif currentTurPos > 8:
            currentTurPos = 8

        if mainTankX-(tankWidth/2) <= xlocation+barrier_width:
            mainTankX += 5
        
        tank(mainTankX,mainTankY,currentTurPos)

        barrier(xlocation,randomHeight,barrier_width)
        
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
game_loop()
