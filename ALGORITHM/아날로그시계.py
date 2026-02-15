def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    answer += count_at_alarm(h2,m2,s2) - count_at_alarm(h1,m1,s1) 
    
    #시작시간이 12시 정각이나 0시 정각인 경우 count + 1 (구간 차 때문에 빠져서 추가해야됨)
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        answer+=1
    return answer

def count_at_alarm(h,m,s):
    total_seconds = h*60*60 + m*60 + s
    #초침이 시침을 추월하는 횟수
    #초침은 12시간에 12*60 = 720 바퀴 회전
    #시침은 12시간에 1바퀴 회전 ==> 12시간에 719바퀴 추월
    overlap_h = total_seconds * 719 // (12*60*60)
    #초침이 분침을 추월하는 횟수
    #초침은 12시간에 12*60 = 720 바퀴 회전
    #분침은 12시간에 12바퀴 회전 ==> 12시간에 708바퀴 추월
    overlap_m = total_seconds * 708 // (12*60*60)
    
    #12시 정각을 지나면
    if total_seconds >= 43200:
        return overlap_h + overlap_m - 1 #초침, 분침, 시침이 모두 겹칠 땐 알람 1번만
    return overlap_h + overlap_m
