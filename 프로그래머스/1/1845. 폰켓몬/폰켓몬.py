def solution(nums):
    hash_map = {}
    num = len(nums) // 2
    
    for n in nums:
        hash_map[n] = hash_map.get(n, 0) + 1
    
    if len(hash_map) >= num:
        return num
    else:
        return len(hash_map)
            
        