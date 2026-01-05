def solution(progresses, speeds):
    answer = []
    time = [(100-progresses[0]) // speeds[0] if (100-progresses[0]) % speeds[0] == 0 else (100-progresses[0]) // speeds[0] + 1]
    
    count = 1
    for i in range(1, len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            if ((100-progresses[i]) // speeds[i]) <= time[-1]:
                count += 1
            else:
                answer.append(count)
                del time[-1]
                time.append((100-progresses[i]) // speeds[i])
                count = 1
        else:
            if ((100-progresses[i]) // speeds[i] + 1) <= time[-1]:
                count += 1
            else:
                answer.append(count)
                del time[-1]
                time.append((100-progresses[i]) // speeds[i] + 1)
                count = 1
    answer.append(count)
     
    return answer