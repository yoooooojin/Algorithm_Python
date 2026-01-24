def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            a = yellow // i
        else:
            continue

        if (2 * a + (i + 2) * 2) == brown:
            if i+2 > a+2:
                answer = [i+2, a+2]
            else:
                answer = [a+2, i+2]
            break
        
    return answer