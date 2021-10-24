import pygame
from pygame.locals import *
import sys
def getSquare(position):
    if position[0]>0 and position[0]<100:
        col=1
    elif position[0]>100 and position[0]<200:
        col=2
    elif position[0]>200:
        col=3
    if position[1]>0 and position[1]<100:
        row=1
    elif position[1]>100 and position[1]<200:
        row=2
    elif position[1]>200:
        row=3

    print((col,row))
    return (col,row)
def drawX(position):
    # draw an X!
    square=getSquare(position)
    print(square)
    if square==(1,1):
        pygame.draw.line(DISPLAYSURF, RED, (0, 0), (100, 100))
        pygame.draw.line(DISPLAYSURF, RED, (100, 0), (0, 100))
    elif square==(2,1):
        pygame.draw.line(DISPLAYSURF, RED, (100, 0), (200, 100))
        pygame.draw.line(DISPLAYSURF, RED, (100, 100), (200, 0))
    elif square==(3,1):
        pygame.draw.line(DISPLAYSURF, RED, (200, 0), (300, 100))
        pygame.draw.line(DISPLAYSURF, RED, (200, 100), (300, 0))
    elif square==(1,2):
        pygame.draw.line(DISPLAYSURF, RED, (0, 100), (100, 200))
        pygame.draw.line(DISPLAYSURF, RED, (0, 200), (100, 100))
    elif square==(2,2):
        pygame.draw.line(DISPLAYSURF, RED, (100, 100), (200, 200))
        pygame.draw.line(DISPLAYSURF, RED, (200, 100), (100, 200))
    elif square == (3, 2):
        pygame.draw.line(DISPLAYSURF, RED, (200, 100), (300, 200))
        pygame.draw.line(DISPLAYSURF, RED, (200, 200), (300, 100))
    elif square == (1,3):
        pygame.draw.line(DISPLAYSURF, RED, (0, 200), (100, 300))
        pygame.draw.line(DISPLAYSURF, RED, (0, 300), (100, 200))
    elif square == (2,3):
        pygame.draw.line(DISPLAYSURF, RED, (100, 200), (200, 300))
        pygame.draw.line(DISPLAYSURF, RED, (100, 300), (200, 200))
    elif square == (3,3):
        pygame.draw.line(DISPLAYSURF, RED, (200, 200), (300, 300))
        pygame.draw.line(DISPLAYSURF, RED, (200, 300), (300, 200))

def drawO(position):
    square=getSquare(position)
    x=square[0]
    x-=1
    y=square[1]
    y-=1
    pygame.draw.circle(DISPLAYSURF,BLACK,(((x*100)+50),50+(y*100)),50,2)



if __name__ == '__main__':
    # Initialize program
    pygame.init()

    # Assign FPS a value
    FPS = 30
    FramePerSec = pygame.time.Clock()

    # Setting up color objects
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Setup a 300x300 pixel display with caption
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Tic-Tac-Toe")

    # Creating Lines and Shapes
    # pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (130, 170))
    # pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (170, 170))
    # pygame.draw.line(DISPLAYSURF, RED, (130, 170), (170, 170))
    # pygame.draw.circle(DISPLAYSURF, BLACK, (100, 50), 30)
    # pygame.draw.circle(DISPLAYSURF, BLUE, (200, 50), 30)
    # pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
    # pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
    pygame.draw.line(DISPLAYSURF,BLACK,(100,300),(100,0))
    pygame.draw.line(DISPLAYSURF, BLACK, (200, 300), (200, 0))
    pygame.draw.line(DISPLAYSURF, BLACK, (300, 100), (0, 100))
    pygame.draw.line(DISPLAYSURF, BLACK, (300, 200), (0, 200))


    # Beginning Game Loop
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                drawX(pygame.mouse.get_pos())
            elif pygame.mouse.get_pressed() == (0,0,1):
                drawO(pygame.mouse.get_pos())
        FramePerSec.tick(FPS)

