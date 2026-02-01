def func1(level, diffs,times):
    takes = times[0]
    for i in range(1,len(diffs)):
        if diffs[i] > level:
            takes += (diffs[i]-level)*(times[i]+times[i-1]) + times[i]
        else:
            takes += times[i]
    return takes

def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = max(diffs)
    
    while left <= right: #이진탐색 
        mid = (left+right)//2
        if func1(mid,diffs,times) <= limit: #소요시간이 제한시간과 같거나 작은 경우
            answer = mid #더 작은 최소레벨이 있을 수 있으니 바로 리턴하지 않고 저장만
            right = mid-1 #이제 더 큰 숫자는 탐색할 필요없으니 right범위 좁힘
        elif func1(mid,diffs,times) > limit: #소요시간이 제한시간보다 큰 경우
            left = mid+1 #최소레벨을 더 큰 숫자 중에서 찾아야 하니 left 증가시킴
    return answer
