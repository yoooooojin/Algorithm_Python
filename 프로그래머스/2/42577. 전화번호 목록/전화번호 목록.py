def solution(phone_book):
    answer = True
    hash_map = {}
    
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            
    return answer