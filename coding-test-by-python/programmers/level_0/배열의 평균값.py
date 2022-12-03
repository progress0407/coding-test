import numpy as np


def solution(numbers):
    return np.mean(numbers)
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f'결과: {result}')
