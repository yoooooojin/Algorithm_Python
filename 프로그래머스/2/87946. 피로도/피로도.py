from itertools import permutations

def solution(k, dungeons):
    count = 0
    reset_k = k
    answer = 0
    
    for r in range(1, len(dungeons) + 1):
        for p in permutations(dungeons, r):
            for need, cost in p:
                if need <= k:
                    k -= cost
                    count += 1
                else:
                    continue
            if count > answer:
                answer = count
            count = 0
            k = reset_k
            
            
    return answer