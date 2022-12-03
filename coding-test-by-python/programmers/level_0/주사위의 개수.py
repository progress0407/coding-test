from functools import reduce


# def solution(box, n):
#     sizes = [s // n for s in box]
#     return reduce(lambda x, y: x * y, sizes)


def solution(box, n):
    w, h, d = [s // n for s in box]
    return reduce(lambda x, y: x * y, (w, h, d))


# solution_result = solution([1, 1, 1], 1)
solution_result = solution([10, 8, 6], 3)
print(f'결과 = {solution_result}')
