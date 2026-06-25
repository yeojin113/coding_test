"""
def solution(array):  
    mode = {}
    
    for num in array:
        if num in mode:
            mode[num] += 1
        else:
            mode[num] = 1
        
    max_num = max(mode.values())
    
    modes = []
    for key, value in mode.items() :
        if value == max_num :
            modes.append(key)
            
    if len(modes) >= 2 :
        return -1
    else :
        return modes[0]
"""

# 답
from collections import Counter

def solution(array):
    counter = Counter(array)

    max_count = max(counter.values())

    if list(counter.values()).count(max_count) > 1:
        return -1

    return max(counter, key=counter.get)