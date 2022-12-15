import re
from collections import deque


# fail
# 처리 불가: 공백, 두 자리수 이상
# def solution(my_string):
#     nums_and_ops = deque(int(ch) if ch.isdigit() else ch for ch in my_string.split(' '))
#
#     print(nums_and_ops)
#     while len(nums_and_ops) != 1:
#         left = nums_and_ops.pop()
#         op = nums_and_ops.pop()
#         right = nums_and_ops.pop()
#         result = 0
#         if op == '+':
#             result = left + right
#         elif op == '-':
#             result = left - right
#         nums_and_ops.appendleft(result)
#     return nums_and_ops[0]


# def solution(my_string):
#     my_string = my_string.replace(' ', '')
#     nums = deque(int(ch) for ch in re.split('\\+|\\-', my_string))
#     ops = deque(c for c in re.split('\\d', my_string) if c not in {''})
#     while len(ops) > 0:
#         left = nums.popleft()
#         right = nums.popleft()
#         op = ops.popleft()
#         result = 0
#         if op == '+':
#             result = left + right
#         elif op == '-':
#             result = left - right
#         nums.appendleft(result)
#     return result


# def solution(my_string):
#     return eval(my_string)


def solution(my_string):
    replace = my_string.replace(' - ', ' + -')
    print(replace)
    split = replace.split(' + ')
    print(split)
    split_ = (int(i) for i in split)
    print(list(split_))
    return sum(split_)



solution_result = solution("3 + 4")
# solution_result = solution(" 3 + 1 - 4")
# solution_result = solution(" 1 - 2-4")
# solution_result = solution("999 - 456 + 123")
print(f'결과 = {solution_result}')
