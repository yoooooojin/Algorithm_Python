def solution(n, lost, reserve):
    answer = 0
    lost.sort(); reserve.sort()
    
    for i in range(1, n + 1):
        if i not in lost:
            answer += 1
    
    for i in lost[:]:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
            answer += 1
            
    for i in lost:
        if (i - 1) in reserve:
            reserve.remove(i - 1)
            answer += 1
        elif (i + 1) in reserve:
            reserve.remove(i + 1)
            answer += 1
            
    return answer