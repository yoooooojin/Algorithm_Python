from itertools import permutations

def solution(k, dungeons):
    count = 0
    reset_k = k
    answer = 0
    
    for p in permutations(dungeons):
        for need, cost in p:
            if need <= k:
                k -= cost
                count += 1
        if count > answer:
            answer = count
        count = 0
        k = reset_k
            
            
    return answer