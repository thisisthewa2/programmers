from collections import deque
def find_oil(land,n,m):
    ry = [0,0,-1,1]
    rx = [-1,1,0,0]
    chunk_size = {}
    chunk_id = 2
    visited = set()
    queue = deque()
    for i in range(n):
        for j in range(m):
            if land[i][j] ==1 and (i,j) not in visited:
                count = 1 #덩어리별 석유량 계산
                visited.add((i,j))
                land[i][j] = chunk_id #한 덩어리란 걸 표시
                queue.append((i,j))
                
                while queue:
                    y,x = queue.popleft()
                    for k in range(4):
                        dy = y + ry[k]
                        dx = x + rx[k]
                        if 0<=dy<n and 0<=dx<m: #land범위안에 있는지 확인
                            if land[dy][dx] ==1 and (dy,dx) not in visited:
                                count += 1 #덩어리별 석유량 계산
                                visited.add((dy,dx))
                                land[dy][dx] = chunk_id #한 덩어리란 걸 표시
                                queue.append((dy,dx))
                chunk_size[chunk_id] = count
                chunk_id+=1
    return chunk_size
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    chunk_size = find_oil(land,n,m)
    col_oil = [0 for _ in range(m)]
    for j in range(m): #열별로 석유량 계산
        col_chunk = set()
        for i in range(n):
            if land[i][j] > 0:
                col_chunk.add(land[i][j]) #덩어리 저장
        for k in col_chunk:
            col_oil[j] += chunk_size[k]
    answer = max(col_oil)

    return answer
