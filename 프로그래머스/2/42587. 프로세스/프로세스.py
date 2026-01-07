def solution(priorities, location):
    answer = 0
    process = []
    
    for i in range(len(priorities)):
        process.append(i)

    while len(process) > 0:
        if priorities[0] == max(priorities):
            answer += 1
            
            if process[0] == location:
                break
                
            del process[0]
            del priorities[0]
        else:
            process.append(process[0])
            priorities.append(priorities[0])
            del process[0]
            del priorities[0]
            
    return answer