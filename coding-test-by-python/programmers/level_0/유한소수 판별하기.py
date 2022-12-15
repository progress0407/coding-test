import math


def solution(a, b):
    gcd = math.gcd(a, b)
    denominator = b // gcd
    for d in range(2, denominator + 1):
        if denominator % d == 0:
            if d % 2 == 0 or d % 5 == 0:
                continue
            else:
                return 2
    return 1


print(f'결과 = {solution(7, 20)}')
print(f'결과 = {solution(11, 22)}')
print(f'결과 = {solution(12, 21)}')


print(f'test = {1000*11/20 % 1 }')
print(f'test = {1000*11/21 % 1 }')
print(f'test = {1000*11/20 % 1 == 0 }')
