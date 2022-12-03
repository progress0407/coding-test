import math


def solution(n):
    sqrt = math.sqrt(math)
    # sqrt = n ** 0.5
    print(sqrt)
    if sqrt.is_integer() is True:
        return 1
    return 2


if __name__ == '__main__':
    solution_result = solution(144)
    print(f'정답: {solution_result}')
