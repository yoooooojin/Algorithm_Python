def solution(name):
    n = len(name)
    move = n - 1
    
    i = 0
    
    for i in range(n):
        nxt = i + 1

        while nxt < n and name[nxt] == 'A':
            nxt += 1
            
        move = min(move, i * 2 + (n - nxt), (n - nxt) * 2 + i)
         
    for c in name:
        if c != 'A':
            move += (min(abs(ord('A') + 26 - ord(c)), abs(ord(c)) - ord('A')))
        else:
            continue
    
    return move