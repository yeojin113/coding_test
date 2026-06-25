# gcd는 math 라이브러리에서 제공하는 함수로 두 수의 최대공약수를 구해줌 
from math import gcd

def solution(numer1, denom1, numer2, denom2):
    
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    g = gcd(numer, denom)
        
    return [numer // g, denom // g]
