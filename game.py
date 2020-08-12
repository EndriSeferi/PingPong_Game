import pygame
from ball import *
from objects import *
import random
import time
pygame.init()

#Setting up the window
screenHeight = 700
screenWidth = 1000
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")
myfont = pygame.font.SysFont("inkfree", 20)
font = pygame.font.SysFont(
    "inkfree", 40)


class Game:
    def reset(self, player1, player2, ball):
        player1.x = 5
        player1.y = screenHeight/2
        player2.x = screenWidth-15
        player2.y = screenHeight/2
        ball.x = int(screenWidth/2)
        ball.y = int(screenHeight/2)


#Initialization of different variables
run = True
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_aquamarine = (41, 165, 218)
color_red = (220, 50, 73)
color_purple = (175, 50, 220)
color_random = (random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255))

player = Player1()
player2 = Player2()
ball = Ball()
game = Game()


while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Drawing game
    win.fill(color_aquamarine)
    pygame.draw.rect(win, color_black, (5, 50,
                                        screenWidth-10, screenHeight-55))
    pygame.draw.rect(win, color_red, (player.x, player.y,
                                      player.width, player.height))
    pygame.draw.rect(win, color_purple, (player2.x, player2.y,
                                         player2.width, player2.height))
    pygame.draw.circle(win, color_random, (ball.x, ball.y),
                       ball.radius, ball.radius)
    ball.move(player.x, player.y, player2.x, player2.y)
    player.move()
    player2.move()

    #if player 1 scores shoot the ball on the other direction
    if ball.is_dead and ball.right and (player.score < 3 or player2.score < 3):
        player.score += 1
        ball.is_dead = False
        ball.vel = -8
        ball.angle = 0
        color_random = (random.randint(0, 255), random.randint(0, 255),
                        random.randint(0, 255))
        game.reset(player, player2, ball)

    #if player 2 scores shoot the ball on the other direction
    if ball.is_dead and (player.score < 3 or player2.score < 3):
        player2.score += 1
        ball.is_dead = False
        ball.vel = 8
        ball.angle = 0
        color_random = (random.randint(0, 255), random.randint(0, 255),
                        random.randint(0, 255))
        game.reset(player, player2, ball)

    #If player 1 wins
    if player.score == 3:
        win.blit((font.render('Player 1 won', 1, (color_aquamarine))),
                 (screenWidth/2-100, screenHeight/2-100))
        win.blit((font.render('Press Space to play again...', 1, (color_aquamarine))),
                 (300, screenHeight/2-60))
        ball.vel = 0
    #If player 2 wins
    if player2.score == 3:
        win.blit((font.render('Player 2 won', 1, (color_white))),
                 (screenWidth/2-100, screenHeight/2-100))
        win.blit((font.render('Press Space to play again...', 1, (color_white))),
                 (300, screenHeight/2-60))
        ball.vel = 0


    keys = pygame.key.get_pressed()

    #Restart Game when press space
    if keys[pygame.K_SPACE]:
        game.reset(player, player2, ball)
        player.score = 0
        player2.score = 0
        if ball.right:
            ball.vel = 8
        else:
            ball.vel = -8

    #Abilities to use
    if keys[pygame.K_q]:
        q = True
        player2.counter += 1
        if (ball.x+ball.radius >= player2.x and ball.x+ball.radius <= player2.x+10) and (ball.y >= player2.y and ball.y <= player2.y+90) and q and player2.counter <= 100:
            ball.vel = -20
            q = False
    if keys[pygame.K_l]:
        l = True
        player.counter += 1
        if (ball.x-ball.radius >= player.x and ball.x-ball.radius <= player.x+10) and (ball.y >= player.y and ball.y <= player.y+90) and l and player.counter <= 100:
            ball.vel = 20
            l = False
   
    #Navbar gui
    player1_score = "Score: "+str(player.score)
    player2_score = "Score: "+str(player2.score)
    player1_score_txt = myfont.render(player1_score, 1, (0, 0, 0))
    player2_score_txt = myfont.render(player2_score, 1, (0, 0, 0))
    win.blit((font.render('Ping Pong', 1, (0, 0, 0))),
             (screenWidth/2-100, -2))
    win.blit(player1_score_txt, (5, 25))
    win.blit((myfont.render('Player 1', 1, (color_black))),
             (5, 8))
    win.blit(player2_score_txt, (screenWidth-120, 25))
    win.blit((myfont.render('Player 2', 1, (color_black))),
             (screenWidth-120, 8))
    win.blit(myfont.render("Hold Q to Strike", 1, (0, 0, 0)), (screenWidth-120, 40))
    win.blit(myfont.render("Hold L to Strike", 1, (0, 0, 0)), (0, 40))

    pygame.display.update()


pygame.quit()
