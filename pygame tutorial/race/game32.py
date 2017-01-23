import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
gray = (120,120,120)
red = (180,0,0)
green = (0,180,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
yellow = (200,200,0)

block_colour = (53,115,225)

car_width = 62

# window size using tuple
gameDisplay = pygame.display.set_mode((display_width,display_height))
# window title
pygame.display.set_caption('A bit Racey')
# specific pygame clock
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

bushImg = pygame.image.load('bush.png')

def stats(count, speed):
    font = pygame.font.SysFont(None, 25)
    dodged_text = font.render('Dodged: ' + str(count), True, black)
    speed_text = font.render('Car Speed: ' + str(round(speed,1)), True, black)
    
    gameDisplay.blit(dodged_text, (0,0))
    gameDisplay.blit(speed_text, (0,25))

def things(thingx, thingy, thingw, thingh, block_colour):
    pygame.draw.rect(gameDisplay, block_colour, [thingx, thingy, thingw, thingh])

# x, start y, end y, thickness
def lane_stripes(linesy, lineey):
    index = 0
    linex = display_width/2

    stripes = []
    while len(stripes) < 18:
        stripes.append('')

    for stripe in stripes:
        pygame.draw.line(gameDisplay, yellow, (linex,linesy), (linex,lineey), 8)
        linesy += 90
        lineey += 90

def draw_bushes(bushx, bushy, bushw, bushh):    
    gameDisplay.blit(bushImg, [bushx, bushy, bushw, bushh])
    gameDisplay.blit(bushImg, [bushx*2.55, bushy, bushw, bushh])

def car(x,y):
    # draw to background (item, where on screen)
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()

    time.sleep(2)

def crash():
    message_display('You Crashed')
    game_loop()

def quit_game():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # box right side > mouse x position > box left side
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action!= None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    # button text
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+w/2),(y+h/2))
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('A bit Racey', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150,450,100,50, green, bright_green, game_loop)
        button("QUIT", 550,450,100,50, red, bright_red, quit_game)
            
        pygame.display.update()
        clock.tick(15)

def game_loop():
    # better to make initialise function? but don't know
    # how to bring values back here for use anyway
    
    x = (display_width * 0.45)
    # image goes from top right, so having it 0 will draw off-screen
    y = (display_height * 0.8)
    # for movement
    x_change = 0
    car_speed_mod = 1

    thing_speed = 5
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -600

    # extras
    linesy = 0
    lineey = 30

    bushx = display_width/4
    bushy = 50
    bushw = 60
    bushh = 60
    bush_speed = 10

    dodged = 0

    # init false, can set true to reset
    gameExit = False

    while not gameExit:
        # any event; mouse, keys, etc per frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change * car_speed_mod

        # must be first or will draw over the car
        gameDisplay.fill(gray)
        # road lanes
        pygame.draw.line(gameDisplay, yellow, (300,0), (300,display_height), 8)
        pygame.draw.line(gameDisplay, yellow, (500,0), (500,display_height), 8)
        lane_stripes(linesy, lineey)
        # move them
        linesy += 10 * car_speed_mod
        lineey += 10 * car_speed_mod
        # reset lines
        if linesy > display_height:
            linesy = 0
            lineey = 30
        # bushes on side
        draw_bushes(bushx, bushy, bushw, bushh)
        bushy += bush_speed * car_speed_mod
        # reset bush
        if bushy > display_height:
            bushy = 0

        # blocks
        things(thing_startx, thing_starty, thing_width, thing_height, block_colour)
        thing_starty += thing_speed
        
        # draw to screen
        car(x,y)
        # score
        stats(dodged, car_speed_mod)

        if x > display_width - car_width or x < 0:
            crash()

        # reset falling block position
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = thing_startx = random.randrange(0, display_width - thing_width)
            # increases
            dodged += 1
            thing_speed += 0.5
            thing_width = random.randint(90,160)
            if dodged % 3 == 0:
                car_speed_mod += 0.3

        # collision of block
        # thing_starty + thing_height = bottom of the block...69 = car height
        #if y < thing_starty + thing_height and thing_starty < display_height - 69:
         #   if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
          #      crash()
        
        # updates whole surface (window) or parameters
        pygame.display.update()
        # Frames per second
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
