'''author @Rhythm KC'''
from queue import Queue

default_maze =   [["X",'X','X','X','X','X','X','X','X','X','X','X','X'],
["$",".",".",".",".",".",".",".",".",".",".",".","X"],
["X",".","X","X","X",".","X","X","X",".","X",".","X"],
["X",".","X",".","X",".",".",".","X",".","X",".","X"],
["X",".","X",".","X","X","X",".","X","0","X",".","X"],
["X",".",".",".",".",".",".",".",".",".",".",".","X"],
["X","X","X","X","X","X","X","X","X","X","X","X","X"]]

FINISH = "0"
START = "$"
EMPTY = "."
BLOCKED ="X"

def find_start(start=None):
    '''
        checks if a start point exists in the given maze
    '''
    for i, valuex in enumerate(default_maze):
        for j, valuey in enumerate(valuex):
            if valuey == "$":
                start =[i,j]
                return start
    raise Exception()


def get_neighbour(current_index):
    '''
        For the gievn current index it finds it we can
        move to the adjecent cells
    '''
    no_col = len(default_maze[0])
    no_row = len(default_maze)
    neighbours = []
    current_row = current_index[0]
    current_col = current_index[1]
    if current_row + 1 != no_row:
        if default_maze[current_row+1][current_col]!=BLOCKED:
            neighbours.append([current_row+1,current_col])
    if current_row -1 != -1:
        if default_maze[current_row-1][current_col]!=BLOCKED:
            neighbours.append([current_row-1,current_col])
    if current_col+ 1 != no_col:
        if default_maze[current_row][current_col+1]!=BLOCKED:
            neighbours.append([current_row,current_col+1])
    if current_col-1 != -1:
        if default_maze[current_row][current_col-1]!=BLOCKED:
            neighbours.append([current_row,current_col-1])
    return neighbours

def solve_maze_bfs(start:list):
    '''
        Given a start point to a maze of n*n
        the function finds the shortest path from start to a finish point if possible
        @return bool true if path exists else false
    '''
    visited =[]
    paths=[]
    queue = Queue()
    queue.put([start])
    while not queue.empty():

        current_path = queue.get()
        current_node = current_path[-1]

        if current_node not in visited:
            visited.append(current_node)
            paths.append(current_path)
        
        if default_maze[current_node[0]][current_node[1]]  == FINISH:
            return (True, paths)
        neighbours = get_neighbour(current_node) 
        for neighbour in neighbours:
            if neighbour not in current_path:
                new_path = current_path + [neighbour]
                queue.put(new_path)
    return (False, paths)

def solve_maze_dfs(start:list):
    '''
        solves maze using DFS
    '''
    visited = []
    paths =[]
    stack = [[start]]
    while len(stack) != 0:
        current_path = stack.pop(-1)
        current_node = current_path[-1]

        if current_node  in visited:
            continue
        
        visited.append(current_node)
        paths.append(current_path)

        if default_maze[current_node[0]][current_node[1]] == FINISH:
            return (True, paths)
        neighbours = get_neighbour(current_node)

        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(current_path + [neighbour])
    return False, paths