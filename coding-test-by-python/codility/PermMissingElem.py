# from functools import reduce
# import numpy
# from numpy import max


def solution(A):
    # max = numpy.max(A)
    # max = sorted(A, reverse=True)[0]
    if len(A) == 0:
        return 1
    max_val = max(A)
    ns = list(n for n in range(1, max_val + 1) if n not in A)
    return ns[0]


print(f'결과: {solution([2, 3, 1, 5])}') # 4
print(f'결과: {solution([])}') # 1
print(f'결과: {solution([2])}') # 1
