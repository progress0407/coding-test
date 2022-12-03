def solution(target):
    return [n for n in range(1, target + 1) if target % n == 0]


solution_result = solution(24)
print(f'결과 = {solution_result}')
