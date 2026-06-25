def solution(array):  
    mode = {}
    n = 0
    
    for num in array:
        if num in mode:
            mode[num] += 1
        else:
            mode[num] = 1
    
    for num in array :
        mode[num] += 1
        
    max_num = max(mode.values())
    
    list = []
    for key, value in mode.items() :
        if value == max_num :
            list.append(key)
    if len(list) >= 2 :
        return -1
    else :
        return list[0]