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
    canvas.fill(pygame.Color(0,0,0,1))
    for coor in path:
        yVal = coor[0] 
        xVal = coor[1]
        rect = pygame.Rect(xVal*BLOCK_WIDTH,yVal*BLOCK_WIDTH,BLOCK_WIDTH,BLOCK_WIDTH)
        pygame.draw.rect(canvas,(0,45,45,0.7),rect)
    if finalMessage != None:
        canvas.blit(finalMessage, finalMessage.get_rect())

def option_display(window, heigth, width):
    '''
        creates two buttons that helps users select if he wants to Use BFS or DFS
    '''
    pygame.draw.rect(window, (50,50,50),[width//2 -100,heigth//2, 50,30])
    pygame.draw.rect(window, (50,50,50),[width//2 +50,heigth//2, 50,30])
    
    smallfont = pygame.font.Font(None,16) 
    bfsText = smallfont.render('BFS' , True , (250,250,250))
    dfsText = smallfont.render('DFS' , True , (250,250,250))
    window.blit(bfsText, (width//2 -90, heigth//2 + 10))
    window.blit(dfsText, (width//2 +60, heigth//2 + 10))

def check_click_dfs(width, height, mousePos):
    '''
        checks if DFS button was clicked 
    '''
    return ((width//2+50)< mousePos[0]<(width//2+100) and (height//2 < mousePos[1] < height//2 +30))
def check_click_bfs(width, height, mousePos):
    '''
        checks if BFS button was clicked 
    '''
    return ((width//2-100)< mousePos[0]<(width//2-50) and (height//2 < mousePos[1] < height//2 +30))

def setup_window(mazeboard):
    '''
        Does the intital setup for the Graphics 
    '''
    WINDOW_WIDTH = len(mazeboard[0]) * BLOCK_WIDTH 
    WINDOW_HEIGHT = len(mazeboard) * BLOCK_WIDTH 
    display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) # creating a window 
    draw(mazeboard,display) # drawing the intital unexplored maze
    option_display(display,WINDOW_HEIGHT, WINDOW_WIDTH)
    return WINDOW_WIDTH, WINDOW_HEIGHT, display

def main():
    '''
        the main function
    '''
    option_selected = False
    mazeboard = maze.default_maze
    solved,paths = None,None 
    text = None
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW= setup_window(mazeboard) #setting up initial window



    # these condition set final text 
    #if solved:
    #    text = FONT.render("Found shortest Path",False,pygame.Color(0,255,0,1),pygame.Color(0,0,0,0))
    #    text.get_rect().center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    #else:
    #    text = FONT.render("No path found",False,pygame.Color(255,0,0,1),pygame.Color(0,0,0,0))
    #    text.get_rect().center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

    # the main loop
    while(True): 
        fps_clock.tick_busy_loop(5) # setting fram rate to 10FPS
        
        for events in pygame.event.get():
            if(events.type == pygame.QUIT):
               pygame.quit()
               sys.exit()
            if (events.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                if not option_selected and check_click_bfs(WINDOW_WIDTH, WINDOW_HEIGHT, mousePos):
                    solved, paths = maze.solve_maze_bfs(maze.find_start())
                    option_selected = True 
                if not option_selected and check_click_dfs(WINDOW_WIDTH,WINDOW_HEIGHT, mousePos):
                    solved, paths = maze.solve_maze_dfs(maze.find_start())
                    option_selected = True 
        #drawing each path on by one 
        if option_selected:
            if len(paths) !=0:
                finalMessage  = None
                if(len(paths) ==1):
                    finalMessage = text
                draw_path(paths.pop(0),WINDOW, finalMessage)
                draw(mazeboard,WINDOW)
        pygame.display.update()





main()