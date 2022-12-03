import math


def solution(slice, n):
    return math.ceil(n / slice)


if __name__ == '__main__':
    result = solution(5_500)
    print(f'결과: {result}')
