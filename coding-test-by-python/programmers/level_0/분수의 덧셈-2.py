import math

# 대수적 특성을 이용해서 풀이

def solution(denum1, num1, denum2, num2):

    denum = denum1*num2 + denum2*num1
    num = num1*num2

    gcd = math.gcd(denum, num)

    return [denum // gcd, num // gcd]


print(f'결과: {solution(1, 2, 3, 4)}')  # [5,4]
