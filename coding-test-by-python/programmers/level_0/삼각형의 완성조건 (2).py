# def solution(sides):
#     max_of_two = max(sides)
#     min_of_two = min(sides)
#
#     max_candidate = max_of_two + min_of_two - 1
#     min_candidate = min_of_two
#
#     for x in reversed(range(1, min_of_two + 1)):
#         if x + min_of_two > max_of_two:
#             min_candidate = x
#
#     cnt = 0
#     for x in range(min_candidate, max_candidate + 1):
#         if x + min_of_two > max_of_two:
#             cnt += 1
#
#     return cnt


# 생각을 열심히 해서 푼 방법
def solution(sides):
    max_of_two = max(sides)
    min_of_two = min(sides)

    max_side = max_of_two + min_of_two - 1
    min_side = max_of_two - min_of_two + 1

    return max_side - min_side + 1


print(f'결과 = {solution([1, 2])}')  # 1
print(f'결과 = {solution([3, 6])}')  # 5
print(f'결과 = {solution([11, 7])}')  # 13
