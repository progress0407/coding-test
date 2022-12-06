# 나의 풀이: 원소 하나씩 제거
# def solution(before, after):
#     after = list(after)
#     for ch in before:
#         try:
#             after.remove(ch)
#         except ValueError:
#             pass
#
#     if len(after) == 0:
#         return 1
#     return 0

# 정렬하기!
def solution(before, after):
    if sorted(before) == sorted(after):
        return 1
    return 0


solution_result = solution("olleh", "hello")
print(solution_result)
