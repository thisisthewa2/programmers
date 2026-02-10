from collections import deque
def changeable(word1,word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count +=1
    return count == 1
def solution(begin, target, words):
    answer = 0
    step = 0 # 최소 단계 저장
    queue = deque([(begin, step)])
    visited = set([begin])
    
    while queue:
        curr, step = queue.popleft()
        if curr == target:
            return step
        for word in words:
            if changeable(curr,word) and word not in visited:
                step+=1
                queue.append((word,step))
                visited.add(word)
                
    return answer
