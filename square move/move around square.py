import pygame
import random

pygame.init()

display_width = 800
display_height = 600

green = (0,180,0)
blue = (0,50,180)
background_c = (120,120,120)

gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

def draw_bullet(bulletx, bullety):
    bulletw = 20
    bulleth = 20
    pygame.draw.rect(gameDisplay, blue, [bulletx, bullety, bulletw, bulleth])

def bullet_shoot(bullets, bullet_directions):
    bullet_speed = 30
    xy = 0
    x = 0
    y = 0
    
    i = 0
    bullets_index = 0

    for bullet in bullets:
        if i > len(bullet_directions)-1:
            i = 0
        if bullet_directions[i] > 0:          # up left
            if xy == 0:
                x = bullet - bullet_speed
                bullet = x
                xy += 1
            if xy == 1:
                y = bullet - bullet_speed
                bullet = y
                bullets_index += 2
                i += 1
            
        elif bullet_directions[i] == 2:        # up
            pass
            #if xy == 0:
                #y -= bullet_speed
                #i += 1
        elif bullet_directions[i] == 3:        # up right
            x += bullet_speed
            y -= bullet_speed
        elif bullet_directions[i] == 4:        # right
            x += bullet_speed
        elif bullet_directions[i] == 5:        # down right
            x += bullet_speed
            y += bullet_speed
        elif bullet_directions[i] == 6:        # down
            y += bullet_speed
        elif bullet_directions[i] == 7:        # down left
            x -= bullet_speed
            y += bullet_speed
        elif bullet_directions[i] == 8:        # left
            x -= bullet_speed

        if xy == 1:
            xy = 0
            draw_bullet(x,y)
            pygame.display.update()
            print(x,y)
            clock.tick(1)
        
    #return x, y

def get_bullet_direction():
    direc = random.randint(1,8)

    if direc == 1:          # up left
        return 1
    elif direc == 2:        # up
        return 2
    elif direc == 3:        # up right
        return 3
    elif direc == 4:        # right
        return 4
    elif direc == 5:        # down right
        return 5
    elif direc == 6:        # down
        return 6
    elif direc == 7:        # down left
        return 7
    else:        # left
        return 8
    
def draw_block(blockx, blocky, blockw, blockh):
    pygame.draw.rect(gameDisplay, green, [blockx, blocky, blockw, blockh])

def game_loop():
    block_speed = 15
    blockx = display_width/2
    blocky = display_height/2
    blockw = 80
    blockh = 80
    x_change = 0
    y_change = 0

    bullets = []
    bullet_directions = []
    bullets_active = 0

    while True:
        bulletx = blockx + blockw/2 - blockw/8
        bullety = blocky + blockh/2 - blockh/8
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= block_speed
                if event.key == pygame.K_RIGHT:
                    x_change += block_speed
                if event.key == pygame.K_UP:
                    y_change -= block_speed
                if event.key == pygame.K_DOWN:
                    y_change += block_speed
                if event.key == pygame.K_SPACE:
                    bullets_active += 1
                    
                    bullets.append(bulletx)
                    bullets.append(bullety)
                    
                    #bulx_change, buly_change = bullet_direction()
                    bullet_directions.append(get_bullet_direction())

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP:
                    y_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = 0

        # don't move off screen
        if blockx + blockw + x_change < display_width and blockx + x_change > 0:
            blockx += x_change
        if blocky + blockh + y_change < display_height and blocky + y_change > 0:
            blocky += y_change

        # fire bullet in the random direction
        if bullets_active > 0:
            bullet_shoot(bullets, bullet_directions)
        
##        if bullet_active > 0:
##            bulletx += bulx_change
##            bullety += buly_change
            
##        if bulletx < 0 or bulletx > display_width or bullety < 0 or bullety > display_height:
##            bulletx = blockx + blockw/2 - blockw/8
##            bullety = blocky + blockh/2 - blockh/8
##            bullet_active = 0

        gameDisplay.fill(background_c)
        
        draw_block(blockx, blocky, blockw, blockh)
        #draw_bullet(bulletx, bullety)

        pygame.display.update()

        clock.tick(30)

game_loop()
pygame.quit()
quit()
