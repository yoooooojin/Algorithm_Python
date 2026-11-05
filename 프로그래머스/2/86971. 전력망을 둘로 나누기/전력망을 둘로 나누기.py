from collections import deque

def count(start, graph, cut_a, cut_b):   
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if (node, nxt) in [(cut_a, cut_b), (cut_b, cut_a)]:
                continue
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return len(visited)

def solution(n, wires):
    answer = 100000
    
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for wire in wires:
        cut_a = wire[0]
        cut_b = wire[1]
        
        one = count(wire[0], graph, cut_a, cut_b)
        another = count(wire[1], graph, cut_a, cut_b)
        
        if abs(one - another) < answer:
            answer = abs(one - another)
        
    return answer