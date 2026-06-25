""" 
def solution(array):
    for i in range(len(array)) :
        for j in range(i+1, len(array)) : 
            if array[i] > array[j] :
                array[i], array[j] = array[j], array[i]
    
    return array[len(array) // 2] 
"""

# 쉽게는
def solution(array):
    return sorted(array)[len(array) // 2]
