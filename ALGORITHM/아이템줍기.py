from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    grid = [[0]*MAX for _ in range(MAX)]
    for rect in rectangle:
        x1,y1,x2,y2=rect[0]*2, rect[1]*2, rect[2]*2, rect[3]*2
        for x in range(x1,x2+1):
            grid[y1][x] = 2
            grid[y2][x] = 2
            
    for rect in rectangle:
        x1,y1,x2,y2=rect[0]*2, rect[1]*2, rect[2]*2, rect[3]*2
        for y in range(y1,y2+1):
            grid[y][x1] = 2
            grid[y][x2] = 2
    
    for rect in rectangle:
        x1,y1,x2,y2=rect[0]*2, rect[1]*2, rect[2]*2, rect[3]*2
        for y in range(y1+1,y2):
            for x in range(x1+1,x2):
                grid[y][x] = 1
                
    start = (characterX*2, characterY*2)
    end = (itemX*2, itemY*2)
    queue = deque()       
    visited = [[False]*MAX for _ in range(MAX)]
    queue.append((start[0],start[1],0))
    visited[start[1]][start[0]] = True
    
    directions =[(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        x, y, dist = queue.popleft()
        
        if x == end[0] and y == end[1]:
            return dist//2
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<MAX and 0<=ny<MAX:
                if not visited[ny][nx] and grid[ny][nx]==2:
                    visited[ny][nx] = True
                    queue.append((nx,ny,dist+1))
    return -1
