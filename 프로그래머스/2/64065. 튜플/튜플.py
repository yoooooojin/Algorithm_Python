def solution(s):
    s = s[2:-2].split("},{")
    
    sets = []
    for char_set in s:
        sets.append(list(map(int, char_set.split(','))))
    
    sets.sort(key=len)
    
    answer = []
    seen = set()
    
    for current_set in sets:
        for num in current_set:
            if num not in seen:
                answer.append(num)
                seen.add(num)
                break  
                
    return answer