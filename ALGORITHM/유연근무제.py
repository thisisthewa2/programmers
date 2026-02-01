def solution(schedules, timelogs, startday):
    answer = len(schedules)
    schedules = list(map(lambda x:x//100*60+x%100,schedules))
    timelogs =  list(map(lambda row: list(map(lambda x:x//100*60+x%100, row)),timelogs))
    
    for i in range(len(schedules)):
        for j in range(len(timelogs[i])): #timelogs의 길이(직원 수)가 아닌 해당 직원이 출근한 요일(행)만큼 순회해야됨.
            if (startday + j)%7==0 or (startday + j)%7==6:
                continue
            if timelogs[i][j] - schedules[i] > 10:
                answer-=1
                break
                
    return answer
