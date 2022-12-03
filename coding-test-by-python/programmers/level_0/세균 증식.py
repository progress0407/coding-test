def solution(n, t):
#     return n * (2 ** t)
    return n << t


solution_result = solution(2, 10)
print(f'결과 = {solution_result}')
