def solution(answers):
    one = []; two = []; three = []
    for _ in range(2000):
        one.extend([1, 2, 3, 4, 5])
    for _ in range(1250):
        two.extend([2, 1, 2, 3, 2, 4, 2, 5])
    for _ in range(1000):
        three.extend([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    one_count = 0; two_count = 0; three_count = 0
    
    for i in range(len(answers)):
        if one[i] == answers[i]:
            one_count += 1
    for i in range(len(answers)):
        if two[i] == answers[i]:
            two_count += 1
    for i in range(len(answers)):
        if three[i] == answers[i]:
            three_count += 1
    
    answer = []
    
    if max(one_count, two_count, three_count) == one_count:
        answer.append(1)
    if max(one_count, two_count, three_count) == two_count:
        answer.append(2)
    if max(one_count, two_count, three_count) == three_count:
        answer.append(3)
    
    return answer