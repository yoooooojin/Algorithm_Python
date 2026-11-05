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
    answer = n
    
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        one = count(a, graph, a, b)
        answer = min(answer, abs(one - (n - one)))
        
    return answer