from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for start,end in tickets:
        graph[start].append(end)
        
    for key in graph:
        graph[key].sort(reverse=True) #pop은 뒤에서 부터 꺼내니 알파벳 역순 정렬

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        answer.append(airport)

    dfs("ICN")
    return answer[::-1]
