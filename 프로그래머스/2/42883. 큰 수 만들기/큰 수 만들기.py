def solution(number, k):
    count = 0
    lst = list(number)
    result = [lst[0]]
    
    for i in range(1, len(lst)):
        while result and lst[i] > result[-1] and count != k:
            result.pop()
            count += 1
        result.append(lst[i])
        
    if count != k:
        result = result[0:-(k-count)]
        
    answer = "".join(result)
    
    return answer