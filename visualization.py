'''
    This file is will visualize the algorithms to solve a maze
    @author Rhythm KC
'''
import maze
import pygame,sys
from pygame.locals import *

pygame.init()# initilizing pygame

fps_clock = pygame.time.Clock()
FPS = 60
BLOCK_WIDTH = 30
FONT = pygame.font.Font(None,32)



def draw(maeze_board, canvas):
    '''
        It draws the maze on the window 
    '''
    blockSize = BLOCK_WIDTH 
    max_height = blockSize * len(maeze_board)
    max_width= blockSize * len(maeze_board[0])
    colors = [pygame.Color(255,0,0,1), pygame.Color(255,255,255,1), pygame.Color(0,255,0,1)]
    x,y = 0,0
    for i in range(0,max_width,blockSize):
        y=0
        for j in range(0, max_height, blockSize):
            #if maeze_board[x][y] == "X":
            if maeze_board[y][x] == ".":
                y+=1
                continue
            rect = pygame.Rect(i,j,blockSize,blockSize)
            color = pygame.Color('black')        
            if maeze_board[y][x] == "X":
                color = colors[1]
            if maeze_board[y][x] == "$":
                color = colors[0]
            if maeze_board[y][x] == "0":
                color = colors[2]
            pygame.draw.rect(canvas,color,rect)
            y+=1
        x +=1

def draw_path(path, canvas,finalMessage=None):
    '''
        takes a path and draws the path on the window 
    '''
    for coor in path:
        yVal = coor[0] 
        xVal = coor[1]
        rect = pygame.Rect(xVal*BLOCK_WIDTH,yVal*BLOCK_WIDTH,BLOCK_WIDTH,BLOCK_WIDTH)
        pygame.draw.rect(canvas,(0,45,45,0.7),rect)
    if finalMessage != None:
        canvas.blit(finalMessage, finalMessage.get_rect())
    pygame.display.update()

def main():
    '''
        the main function
    '''
    looping = True

    mazeboard = maze.default_maze
    solved,paths = maze.solve() # solves the maze and returns all the paths explored and whether path was found or not

    WINDOW_WIDTH = len(mazeboard[0]) * BLOCK_WIDTH 
    WINDOW_HEIGHT = len(mazeboard) * BLOCK_WIDTH 
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) # creating a window 

    draw(mazeboard,WINDOW) # drawing the intital unexplored maze
    pygame.display.update()
    text = None

    # these condition set final text 
    if solved:
        text = FONT.render("Found shortest Path",False,pygame.Color(0,255,0,1),pygame.Color(0,0,0,0))
        text.get_rect().center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    else:
        text = FONT.render("No path found",False,pygame.Color(255,0,0,1),pygame.Color(0,0,0,0))
        text.get_rect().center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    # the main loop
    while(looping): 
        fps_clock.tick_busy_loop(10) # setting fram rate to 10FPS
        
        for events in pygame.event.get():
            if(events.type == pygame.QUIT):
               pygame.quit()
               sys.exit()
        #drawing each path on by one 
        if len(paths) !=0:
            finalMessage  = None
            if(len(paths) ==1):
                finalMessage = text
            draw_path(paths.pop(0),WINDOW, finalMessage)

        WINDOW.fill(pygame.Color(0,0,0,1))
        draw(mazeboard,WINDOW)





main()