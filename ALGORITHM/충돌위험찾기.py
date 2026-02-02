from collections import Counter
#def get_risks
def get_all_path(points,route): #한 로봇의 전체 경로를 구하는 함수
    all_path = []
    for i in range(len(route)-1):
        path = get_path(points[route[i]-1], points[route[i+1]-1])
        if i==0:
            all_path.extend(path) #iterable요소를 꺼내어 저장하는 extend를 사용해야 get_path함수를 호출하며 부수적으로 얻은 겉껍데기 하나를 없앨 수 있음
        else:
            all_path.extend(path[1:])
    return all_path

def get_path(start,end): #바로 다음 지점까지의 경로를 구하는 함수
    path = [start]
    r, c = start
    while r!= end[0]:
        if r>end[0]:
            r-=1
            path.append([r,c])
        elif r<end[0]:
            r+=1
            path.append([r,c])
    while c!= end[1]:
        if c>end[1]:
            c-=1
            path.append([r,c])
        elif c<end[1]:
            c+=1
            path.append([r,c])
    return path

def solution(points, routes):
    answer = 0
    # print(get_path([1,1],[3,3]))
    # print(get_all_path(points,[1,3]))
    all_robots_path = [] # 모든 로봇의 경로를 저장
    for route in routes:
        all_robots_path.append(get_all_path(points,route))
    
    #최대 시간 구하기
    max_time = max(len(path) for path in all_robots_path)
    #충돌위험 구하기
    for t in range(max_time):
        positions = [] # 매 시간마다 각 로봇의 위치를 저장
        for robot_path in all_robots_path:
            if t < len(robot_path): # 아직 운행중인 로봇만
                positions.append(robot_path[t])
                
        positions_count = Counter(tuple(pos) for pos in positions)
        answer+=sum(1 for count in positions_count.values() if count>=2)

    return answer
