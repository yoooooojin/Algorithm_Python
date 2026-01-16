import heapq

def solution(operations):
    answer = []
    heap = []
    
    for i in operations:
        if i.startswith("I"):
            heapq.heappush(heap, int(i[2:]))
        elif i == "D -1":
            if len(heap) > 0:
                heapq.heappop(heap)   
        else:
            if len(heap) > 0:
                max_heap = [-x for x in heap]
                heapq.heapify(max_heap)
                heapq.heappop(max_heap)
                heap = [-x for x in max_heap]
                heapq.heapify(heap)
    
    if len(heap) == 0:
        answer = [0, 0]
    else:
        min_num = heap[0]
        max_heap = [-x for x in heap]
        heapq.heapify(max_heap)
        max_num = max_heap[0]
        answer = [-max_num, min_num]
        
        
    return answer