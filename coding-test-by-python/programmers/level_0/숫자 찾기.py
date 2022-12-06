# def solution(num, k):
#     num_list = list(map(lambda x: int(x), list(str(num))))
#     for i in num_list:
#         if i == k:
#             return num_list.index(k) + 1
#     return -1

# def solution(num, k):
#     target = str(k)
#     num_str = str(num)
#
#     if target not in num_str:
#         return -1
#     return num_str.find(target) + 1


def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1


solution_result = solution(29183, 1)
print(f'결과 = {solution_result}')
