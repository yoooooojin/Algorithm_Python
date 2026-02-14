def solution(prices):
    answer = []
    time = 0
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            time += 1

            if prices[i] > prices[j]:
                break

        answer.append(time)
        time = 0
        
    return answer