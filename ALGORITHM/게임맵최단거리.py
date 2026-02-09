from collections import deque
def solution(maps):
    answer = 0
    n,m = len(maps),len(maps[0]) #n은 행의 개수 (y축길이)
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    queue = deque([(0,0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        y,x = queue.popleft()
        if x == m-1 and y == n-1:
            answer = maps[y][x]
            return answer
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maps[ny][nx]!=0:
                    visited[ny][nx] = True
                    queue.append((ny,nx))
                    maps[ny][nx] = maps[y][x] + 1
    answer = -1 
    return answer
