# def solution(numbers, direction):
#     result = []
#     if direction == "left":
#         [result.append(c) for c in numbers[1:]]
#         result.append(numbers[0])
#     elif direction == "right":
#         result.append(numbers[-1])
#         [result.append(c) for c in numbers[:-1]]
#     return result


# from collections import deque


# def solution(numbers, direction):
#     numbers = deque(numbers)
#     if direction == 'right':
#         numbers.rotate(1)
#     else:
#         numbers.rotate(-1)
#     return list(numbers)


def solution(numbers, direction):
    if direction == 'right':
        return [numbers[-1]] + numbers[0:-1]
    else:
        return numbers[1:] + [numbers[0]]


# solution_result = solution([1, 2, 3], 'right')
solution_result = solution([1, 2, 3], 'left')
print(f'결과 = {solution_result}')
