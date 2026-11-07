from itertools import product

def solution(word):
    lst = ['A', 'E', 'I', 'O', 'U']
    
    for p in product("AEIOU", repeat=2):
        lst.append("".join(p))

    for p in product("AEIOU", repeat=3):
        lst.append("".join(p))
        
    for p in product("AEIOU", repeat=4):
        lst.append("".join(p))
        
    for p in product("AEIOU", repeat=5):
        lst.append("".join(p))

    lst.sort()
    
    for i, v in enumerate(lst):
        if v == word:
            answer = i + 1
    
    return answer
