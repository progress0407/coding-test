from collections import deque


# def solution(numbers, k):
#     size = len(numbers)
#     for i in range(0, 2 * k, 2):
#         val = numbers[i % size]
#     return val


# def solution(numbers, k):
#     size = len(numbers)
#     return numbers[2 * (k - 1) % size]


def solution(numbers, k):
    circular_queue = deque(numbers)
    circular_queue.rotate(-2 * (k - 1))
    return circular_queue[0]


solution_result = solution([1, 2, 3, 4], 2)
print(f'결과 = {solution_result}')
