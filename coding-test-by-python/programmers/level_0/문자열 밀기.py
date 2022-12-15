# from collections import deque


# def solution(A, B):
#     A = deque(A)
#     B = deque(B)

# for count in range(len(A)):
#     if A == B:
#         return count
#     A.rotate()
# return -1

solution = lambda keyword, find_str: (find_str * 2).find(keyword)

print(f'결과 = {solution("hello", "ohell")}')
print(f'결과 = {solution("apple", "elppa")}')
