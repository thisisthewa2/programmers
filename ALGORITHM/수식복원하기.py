def to_base(n,b):
    if n == 0: return "0"
    result = ""
    while n:
        result = str(n%b) + result
        n = n//b
    return result
def solution(expressions):
    answer = []
    possible = set(range(2,10))
    
    for expr in expressions:
        A,op,B,_,C = expr.split()
        for ch in (A+B+C):
            if ch.isdigit():
                possible -= {b for b in possible if b <= int(ch)}
                
    for expr in expressions:
        A,op,B,_,C = expr.split()
        if C!="X":
            for b in list(possible):
                left = int(A,b) + int(B,b) if op =="+" else int(A,b) - int(B,b)
                right = int(C,b)
                if left!=right:
                    possible.discard(b)
    
    for expr in expressions:
        A,op,B,_,C = expr.split()
        if C=="X":
            results = set()
            for b in list(possible):
                value = int(A,b) + int(B,b) if op =="+" else int(A,b) - int(B,b)
                results.add(to_base(value,b))
            answer_value = results.pop() if len(results)==1 else "?"
            answer.append(f"{A} {op} {B} {_} {answer_value}")
    return answer
