import heapq

def solution(jobs):
    answer, endTime, i = 0, 0, 0
    total_jobs = len(jobs)
    jobs.sort()
    heap = []
    
    while i < total_jobs or heap:
        while i < total_jobs and endTime >= jobs[i][0]:
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i += 1
        if heap:
            duration, requestTime = heapq.heappop(heap)
            endTime += duration
            answer += (endTime - requestTime)
        else:
            endTime = jobs[i][0]
    
    return answer // total_jobs