def solution(genres, plays):
    answer = []
    hash_map = {}
    data_map = {}
    
    for i in range(len(genres)):
        if genres[i] not in hash_map:
            data_map[genres[i]] = []
            data_map[genres[i]].append(i)
        else:
            data_map[genres[i]].append(i)
        
        hash_map[genres[i]] = hash_map.get(genres[i], 0) + plays[i]
        
    sorted_hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
  
    for v in data_map.values():
        while len(v) > 2:
            min = 100000
            for i in v:
                if min > plays[i]:
                    min = plays[i]
                    min_index = i   
            v.remove(min_index)
           
        if len(v) > 1:
            if plays[v[0]] < plays[v[1]]:
                v[0], v[1] = v[1], v[0]
            

    
    for k in sorted_hash_map.keys():
        for i in data_map[k]:
            answer.append(i)
        
    return answer