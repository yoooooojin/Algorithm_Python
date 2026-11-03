def solution(sizes):   
    width = 0
    height = 0
    
    for size in sizes:
        if size[0] >= size[1]:
            if size[0] >= width:
                width = size[0]
            if size[1] >= height:
                height = size[1]
        else:
            if size[0] >= height:
                height = size[0]
            if size[1] >= width:
                width = size[1]
                
    
    return width * height