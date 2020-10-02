
import pygame
import math
import time
pygame.init()  # initialising the game
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Gotta catch 'em all")  # name of the game
yes = True
img1 = pygame.image.load('pikachu.png')  # player1
img2 = pygame.image.load('pokemon.png')  # moving obstacle
img3 = pygame.image.load('zubat.png')  # fixed obstacle
img4 = pygame.image.load('charmander.png')  # player2
px = 350    # x position of player 1
py = 640  # y position of player 1
px1 = 150  # initial position of obstacle1
font = pygame.font.Font('freesansbold.ttf', 32)
o = 0  # initial time
py1 = 307  # y position initial of obst 1
px2 = 450  # position of obstacles
py2 = 440
px3 = 250
py3 = 45
px4 = 450
py4 = 178
g = 0  # variables for checking if the round is over or not
f = 0
h = 0
i = 0
scox = 20  # score board coordinates
scoy = 20
scorev = 0  # variable for score
p1 = 1  # initially player 1 is active
p2 = 0  # initially player2 is inactive
x = 370  # initial position of player 2
y = -5
s = 5  # speed of obstacles for player 1
t = 5  # speed of obstacles for player 2

gameover = False

class youth:
    def score(self, x, y, score):  # function for showing score, start and end
        sco = font.render("SCORE:" + str(score), True, (255, 255, 255))
        screen.blit(sco, (x, y - 10))
        end = font.render("END", True, (255, 255, 255))
        screen.blit(end, (x + 350, y - 10))
        start = font.render("START", True, (255, 255, 255))
        screen.blit(start, (x + 330, y + 640))


    def score1(self, x, y, score):  # function for showing score, start and end
        sco = font.render("SCORE:" + str(score), True, (255, 255, 255))
        screen.blit(sco, (x, y - 10))
        end = font.render("END", True, (255, 255, 255))
        screen.blit(end, (x + 330, y + 640))
        start = font.render("START", True, (255, 255, 255))
        screen.blit(start, (x + 350, y - 10))


    def collision(self, x, y, a, b):  # function for checking collision
        dist = math.sqrt(math.pow(x - a, 2) + math.pow(y - b, 2))
        if(dist < 30):
            return True
        else:
            return False


    def water(self, x, y):
        screen.blit(img2, (x, y))


    def zubat(self, x, y):
        screen.blit(img3, (x, y))


    def player(self, x, y):  # for displaying player1
        screen.blit(img1, (x, y))


    def player2(self, x, y):  # for displaying player 2
        screen.blit(img4, (x, y))





    def message(self, x, y, a, b):
        sco = font.render("GAME OVER , PRESS E TO PLAY AGAIN ", True, (0, 0, 0))
        screen.blit(sco, (50, 150))
        yes = font.render("PLAYER1 SCORE:" + str(a), True, (0, 0, 0))
        screen.blit(yes, (80, 250))
        no = font.render("PLAYER1 TIME:" + str(x) + "ms", True, (0, 0, 0))
        screen.blit(no, (80, 350))
        ok = font.render("PLAYER2 SCORE:" + str(b), True, (0, 0, 0))
        screen.blit(ok, (80, 450))
        nk = font.render("PLAYER2 TIME:" + str(y) + "ms", True, (0, 0, 0))
        screen.blit(nk, (80, 550))
        if a > b:
            po = font.render("PLAYER1 WINS!!!!!!", True, (0, 0, 0))
            screen.blit(po, (80, 50))
        if b > a:
            lo = font.render("PLAYER2 WINS!!!!!!", True, (0, 0, 0))
            screen.blit(lo, (80, 50))
        if b == a and x > y:
            mo = font.render("PLAYER2 WINS!!!!!!!", True, (0, 0, 0))
            screen.blit(mo, (80, 50))
        if b == a and y > x:
            no = font.render("PLAYER1 WINS!!!!!!!", True, (0, 0, 0))
            screen.blit(no, (80, 50))


    def showing(self, x):  # converting milliseconds to seconds and displaying time
        scope = font.render("TIME:" + str(math.floor(x / 1000)
                                        ) + "sec", True, (255, 255, 255))
        screen.blit(scope, (520, 10))

obj = youth()

