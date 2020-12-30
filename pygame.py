import sys, pygame
import os
pygame.init()

size = width, height = 620, 440
speed = [1, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: os._exit(1)

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        if not ballrect.left <= 0:
                                ballrect = ballrect.move(-1, 0)
                                
                if event.key ==  pygame.K_RIGHT:
                        if not ballrect.right >= 620:
                                ballrect = ballrect.move(1, 0)
                                


##        if ballrect.left < 0 or ballrect.right > width:
##                speed[0] = -speed[0]
##        if ballrect.top < 0 or ballrect.bottom > height:
##                speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.update()
