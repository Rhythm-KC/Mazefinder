from collections import deque
from queue import Queue
from typing import List


defalut_maze =   [["X",'X','X','X','X','X','X','X','X','X','X','X','X'],
["$",".",".",".",".",".",".",".",".",".",".",".","X"],
["X",".","X","X","X",".","X","X","X",".","X",".","X"],
["X",".","X",".","X",".",".",".","X",".","X",".","X"],
["X",".","X",".","X","X","X",".","X","X","X",".","X"],
["X",".",".",".",",",".",".",".",".",".","X",".","0"],
["X","X","X","X","X","X","X","X","X","X","X","X","X"]]

FINISH = "0"
START = "$"
EMPTY = "."
BLOCKED ="X"

def findstatstop(start=None):
    for i, valuex in enumerate(defalut_maze):
        for j, valuey in enumerate(valuex):
            if valuey == "$":
                start =[i,j]
                return start
    if start is None:
        raise Exception()

def getNeighbour(currentIndex):
    no_Col = len(defalut_maze[0])
    no_row = len(defalut_maze)
    neighbours = []
    current_row = currentIndex[0]
    current_col = currentIndex[1]
    if(current_row + 1 != no_row):
        if(defalut_maze[current_row+1][current_col]!=BLOCKED):
            neighbours.append([current_row+1,current_col])
    if(current_row -1 != -1):
        if(defalut_maze[current_row-1][current_col]!=BLOCKED):
            neighbours.append([current_row-1,current_col])
    if(current_col+ 1 != no_Col):
        if(defalut_maze[current_row][current_col+1]!=BLOCKED):
            neighbours.append([current_row,current_col+1])
    if(current_col-1 != -1):
        if(defalut_maze[current_row][current_col-1]!=BLOCKED):
            neighbours.append([current_row,current_col-1])

    return neighbours 
        
def solveMazeBFS(start:List):
    vistited =[] 
    queue = Queue()
    queue.put(start)
    while(not queue.empty()):
        currentIndex = queue.get()
        if(currentIndex not in vistited):
            vistited.append(currentIndex)
        if(defalut_maze[currentIndex[0]][currentIndex[1]]  == FINISH):
           return True 
        neighbours = getNeighbour(currentIndex)
        for neighbour in neighbours:
            if(neighbour not in vistited):
                queue.put(neighbour)
    
    return False


def main():
    #try:
        start = findstatstop()
        print(f"{solveMazeBFS(start)} value")
        
    #except Exception:
    #    print("NO WAY TO ENTER THE MAZE")

if __name__ == '__main__':
    main()