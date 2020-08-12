import pygame
screenHeight = 700
screenWidth = 1000


class Ball:
    def __init__(self):
        self.x = int(screenWidth/2)
        self.y = int(screenHeight/2)
        self.radius = 15
        self.vel = 5
        self.angle = 0
        self.right = True
        self.is_dead = False

    def move(self, x, y, x1, y1):
        self.x += self.vel 
        self.y += self.vel*self.angle
        # Bounds top and bottom
        if self.y-self.radius <= 50 and self.right:
            self.angle = 1
        if self.y+self.radius >= screenHeight-5 and self.right:
            self.angle = -1
        if self.y-self.radius <= 50 and not self.right:
            self.angle = -1
        if self.y+self.radius >= screenHeight-5 and not self.right:
            self.angle = 1

        # Bounds score
        if self.x < x and (self.y > 50 and self.y <= y) or (self.x < x and self.y <= screenHeight-5 and self.y >= y+90):
            self.is_dead = True
            self.vel = 0
        if self.x > x1+10 and (self.y > 50 and self.y <= y1) or (self.x > x1+10 and self.y <= screenHeight-5 and self.y >= y1+90):
            self.is_dead = True
            self.vel = 0

        #Hitting the board bounds movement
        if (self.x+self.radius >= x1 and self.x+self.radius <= x1+10) and (self.y >= y1 and self.y <= y1+90):
            if self.y >= y1 and self.y <= y1+40:
                self.angle = 1
            if self.y > y1+40 and self.y <= y1+50:
                self.angle = 0
            if self.y > y1+50 and self.y <= y1+90:
                self.angle = -1
            self.vel = -8
            self.right = False
        if (self.x-self.radius >= x and self.x-self.radius <= x+10) and (self.y >= y and self.y <= y+90):
            if self.y >= y and self.y <= y+40:
                self.angle = -1
            if self.y > y+40 and self.y <= y+50:
                self.angle = 0
            if self.y > y+50 and self.y <= y+90:
                self.angle = 1
            self.right = True
            self.vel = 8
