from collections import Counter
def solution(clothes):
    answer = 1
    category_counts = Counter(category for _, category in clothes)
    for count in category_counts.values():
        answer *= (count+1)
    return answer-1
