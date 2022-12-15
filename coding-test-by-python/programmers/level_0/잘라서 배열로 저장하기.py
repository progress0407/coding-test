import math


# def solution(my_str, n):
#     size = math.ceil(len(my_str) / n)
#     answer = []
#     for i in range(0, size):
#         answer.append(my_str[n * i:n * (i + 1)])
#     return answer


def solution(my_str, n):
    return [my_str[i:i + n] for i in range(0, len(my_str), n)]


solution_result = solution("abc1Addfggg4556b", 6)
print(f'결과 = {solution_result}')
