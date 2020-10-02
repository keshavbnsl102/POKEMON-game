from config import *

while yes:

    while gameover:  # when both players have either died or completed
        screen.fill((255, 0, 255))
        obj.message(p, q, m, n)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # key to play again
                    gameover = False
            if event.type == pygame.QUIT:  # if close button is pressed
                yes = False
                gameover = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yes = False

    if p1:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  # left movement key
            px -= 10
        if keys[pygame.K_RIGHT]:  # right movement key

            px += 10
        if keys[pygame.K_UP]:  # up movement key
            py -= 10
        if keys[pygame.K_DOWN]:  # down movement key
            py += 10
        px1 += s  # speed of moving obstacle
        if px1 > 700:  # if the obstacle reaches end it starts from beginning
            px1 = 0
        if px > 650:  # to prevent the player to go out of screen
            px = 650
        if px < 0:  # to prevent player to go out of screen
            px = 0
        if py > 650:  # to prevent player to go out of screen
            py = 650
        if py < 0:
            py = 0
        if px2 < 0:
            f = 1
        if px2 > 650:
            f = 0
        if f == 0:
            px2 -= s  # if obstacle hits the right end it comes back
        if f == 1:
            px2 += s  # if obstacle hits the left end it moves right
        if(px3 < 0):
            g = 1
        if px3 > 650:
            g = 0
        if g == 0:
            px3 -= s  # if obstacle hits the right end it comes back
        if g == 1:
            px3 += s  # if obstacle hits the left end it moves right
        if(px4 < 0):
            h = 1
        if px4 > 650:
            h = 0
        if h == 0:
            px4 -= s
        if h == 1:
            px4 += s
        screen.fill((0, 0, 255))  # blue colour on the screen
        # for partition I am drawing rectangle
        pygame.draw.rect(screen, (127, 127, 0), (0, 660, 700, 40))
        # for partition I am drawing rectangle
        pygame.draw.rect(screen, (127, 127, 0), (0, 528, 700, 40))
        # for partition I am drawing rectangle
        pygame.draw.rect(screen, (127, 127, 0), (0, 396, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 264, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 132, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 0, 700, 40))
        
        # if player hits the object function returns true
        c1 = obj.collision(px, py, px1, py1)
        c2 = obj.collision(px, py, px2, py2)
        c3 = obj.collision(px, py, 50, 123)
        c4 = obj.collision(px, py, 350, 123)
        c5 = obj.collision(px, py, 270, 255)
        # if player hits the object fnction returns true
        c6 = obj.collision(px, py, 350, 387)
        c7 = obj.collision(px, py, 150, 519)
        c8 = obj.collision(px, py, 450, 519)
        c9 = obj.collision(px, py, 600, 255)
        c10 = obj.collision(px, py, px3, py3)
        c11 = obj.collision(px, py, px4, py4)
        if i == 8 or c1 or c2 or c3 or c4 or c5 \
                or c6 or c7 or c8 or c9 or c10 or c11:
            px = 350
            py = 640
            p1 = 0
            p2 = 1
            i = 0
            m = scorev  # storing the score in a variable
            scorev = 0
            p = pygame.time.get_ticks() - o   # calculating the time of player1
            o = pygame.time.get_ticks()

        if i == 0 and py < 515:  # increasing score by 5 for fixed obstacles
            i = 1
            scorev += 5
        if i == 1 and py < 420:
            scorev += 10  # increasing score by 10 for moving obstacles
            i = 2
        if i == 2 and py < 380:
            scorev += 5  # increasing by 5 for fixed
            i = 3
        if i == 3 and py < 290:  # updating score as before
            scorev += 10
            i = 4
        if i == 4 and py < 250:
            scorev += 5
            i = 5
        if i == 5 and py < 160:
            scorev += 10
            i = 6
        if i == 6 and py < 120:
            scorev += 5
            i = 7
        if i == 7 and py < 30:
            scorev += 10
            i = 8
        obj.player2(370, -5)  # player2 is fixed while player1 is playing
        obj.player(px, py)
        obj.water(px1, py1)  # moving obstacles
        obj.water(px2, py2)
        obj.water(px3, py3)
        obj.water(px4, py4)
        obj.score(scox, scoy, scorev)  # displaying the score
        obj.zubat(50, 123)
        obj.zubat(350, 123)
        obj.zubat(270, 255)  # zubat is the fixed obstacle
        obj.zubat(350, 387)
        obj.zubat(150, 519)
        obj.zubat(450, 519)
        obj.zubat(600, 255)
        obj.showing(pygame.time.get_ticks() - o)
        pygame.display.update()
    if p2:
        keys = pygame.key.get_pressed()  # different keys for player2
        if keys[pygame.K_a]:  # a for left movement
            x -= 10
        if keys[pygame.K_d]:  # d for right movement

            x += 10
        if keys[pygame.K_w]:  # w for up movement
            y -= 10
        if keys[pygame.K_s]:  # s for down movement
            y += 10
        px1 += t  # moving obstacle always moving right
        if px1 > 700:
            px1 = 0
        if x > 650:  # boundary for player2
            x = 650
        if x < 0:  # boundary for player 2
            x = 0
        if y > 650:  # boundary
            y = 650
        if y < 0:  # boundary
            y = 0
        if px2 < 0:
            f = 1
        if px2 > 650:
            f = 0
        if f == 0:
            px2 -= t  # obstacle returns to left after hitting right
        if f == 1:
            px2 += t  # obstacle moving right
        if(px3 < 0):
            g = 1
        if px3 > 650:
            g = 0
        if g == 0:
            px3 -= t  # obstacle returning back
        if g == 1:
            px3 += t  # obstacle moving right
        if(px4 < 0):
            h = 1
        if px4 > 650:
            h = 0
        if h == 0:
            px4 -= t  # obstacle returning back
        if h == 1:
            px4 += t  # obstacle moving right
        screen.fill((0, 0, 255))
        # rectangles for partition
        pygame.draw.rect(screen, (127, 127, 0), (0, 660, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 528, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 396, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 264, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 132, 700, 40))
        pygame.draw.rect(screen, (127, 127, 0), (0, 0, 700, 40))

        # to detect collision calling the collision function in config
        c1 = obj.collision(x, y, px1, py1)
        c2 = obj.collision(x, y, px2, py2)
        c3 = obj.collision(x, y, 50, 123)
        c4 = obj.collision(x, y, 350, 123)
        c5 = obj.collision(x, y, 270, 255)
        c6 = obj.collision(x, y, 350, 387)
        c7 = obj.collision(x, y, 150, 519)
        c8 = obj.collision(x, y, 450, 519)
        c9 = obj.collision(x, y, 600, 255)
        c10 = obj.collision(x, y, px3, py3)
        c11 = obj.collision(x, y, px4, py4)
        if i == 8 or c1 or c2 or c3 or c4 or \
                c5 or c6 or c7 or c8 or c9 or c10 or c11:
            x = 370
            y = -5
            p1 = 1
            p2 = 0
            if m > scorev:  # if player1 has won
                s = s + 5  # increase the obstacle speed in next round
            if scorev > m:    #if player2 has won
                t = t + 5 
            i = 0
            n = scorev
            # o is the time when player 1 completed
            q = pygame.time.get_ticks() - o
            o = pygame.time.get_ticks()
            scorev = 0
            e = 0
            # after player2 has completed then a new screen is displayed
            gameover = True

        if i == 0 and y > 125:
            i = 1
            scorev += 10  # score increases by 10 on passing moving obs
        if i == 1 and y > 165:
            scorev += 5  # score increases by 5 on passing fixed
            i = 2
        if i == 2 and y > 257:
            scorev += 10  # score increases by 10
            i = 3
        if i == 3 and y > 297:
            scorev += 5  # score increases by 5
            i = 4
        if i == 4 and y > 389:
            scorev += 10  # score increases by 10 on passing moving
            i = 5
        if i == 5 and y > 429:
            scorev += 5  # score increases by 5 on passing fixed
            i = 6
        if i == 6 and y > 521:
            scorev += 10  # score increases by 10 on passing moving
            i = 7
        if i == 7 and y > 561:
            scorev += 5
            i = 8
        obj.player2(x, y)
        obj.player(350, 640)  # player1 is fixed while player 2
        obj.water(px1, py1)  # moving obstacles
        obj.water(px2, py2)
        obj.water(px3, py3)
        obj.water(px4, py4)
        obj.score1(scox, scoy, scorev)
        obj.zubat(50, 123)  # fixed obstacles zoobats
        obj.zubat(350, 123)
        obj.zubat(270, 255)
        obj.zubat(350, 387)
        obj.zubat(150, 519)
        obj.zubat(450, 519)
        obj.zubat(600, 255)
        obj.showing(pygame.time.get_ticks() - o)  # showing the time
        pygame.display.update()
