import math


def solution(n):
    return math.ceil(n/7)


# def solution(n):
#     return ((n - 1) // 7) + 1


if __name__ == '__main__':
    result = solution(7)
    print(f'결과: {result}')
