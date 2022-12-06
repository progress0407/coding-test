# 내께 더 깔끔함!

def solution(n):
    result_list = list(filter(lambda x: is_composition_number(x), range(1, n + 1)))
    return len(result_list)


def is_composition_number(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count >= 3


solution_result = solution(15)
print(f'결과 = {solution_result}')
