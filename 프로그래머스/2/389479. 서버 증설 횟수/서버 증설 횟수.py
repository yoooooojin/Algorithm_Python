def solution(players, m, k):
    answer = 0
    n = len(players)
    expire = [0] * (n + k)
    current_servers = 0
    
    for t in range(n):
        current_servers -= expire[t]
        
        needed_total = players[t] // m
        
        if needed_total > current_servers:
            new_servers = needed_total - current_servers
            answer += new_servers
            current_servers += new_servers
            expire[t + k] += new_servers
            
    return answer