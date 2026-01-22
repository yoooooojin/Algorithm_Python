def solution(numbers):
    answer = ''
    str_numbers = [str(n) for n in numbers]

    str_numbers.sort(key=lambda x: x * 10, reverse=True)
    
    for i in range(len(str_numbers)):
        answer += str_numbers[i]
        
    if int(answer) == 0:
        answer = "0"
        
    return answer
