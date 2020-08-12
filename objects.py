import pygame
screenHeight = 700
screenWidth = 1000


class Player1:
    def __init__(self):
        self.x = 5
        self.y = screenHeight/2
        self.height = 90
        self.width = 10
        self.score = 0
        self.counter = 0

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.y > 54:
            self.y -= 8
        if keys[pygame.K_s]and self.y < screenHeight-self.height-5:
            self.y += 8


class Player2:
    def __init__(self):
        self.x = screenWidth-15
        self.y = screenHeight/2
        self.height = 90
        self.width = 10
        self.score = 0
        self.counter = 0

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.y > 54:
            self.y -= 8
        if keys[pygame.K_DOWN]and self.y < screenHeight-self.height-5:
            self.y += 8
