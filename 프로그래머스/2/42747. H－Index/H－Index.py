def solution(citations):
    answer = 0
    
    citations.sort()
    
    for i in range(1, len(citations) + 1):
        list = []
        for j in range(len(citations)):
            if citations[j] >= i:
                list.append(citations[i-1])
            if len(list) == i and i > answer:
                answer = i
    return answer