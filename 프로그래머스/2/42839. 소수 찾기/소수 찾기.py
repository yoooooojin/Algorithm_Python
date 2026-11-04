from itertools import permutations

def solution(numbers):
    answer = 0
    
    lst = list(numbers)
    s = set()
    
    for r in range(1, len(lst) + 1):
        for p in permutations(lst, r):
            num = int("".join(map(str, p)))
            if num in s:
                continue
            else:
                s.add(num)
                
            prime = True
            if num != 0 and num != 1:
                for i in range(2, int(num**0.5) + 1):
                    if num % i != 0:
                        prime = True
                    else:
                        prime = False
                        break
                if prime == True:
                    answer += 1
    
    return answer