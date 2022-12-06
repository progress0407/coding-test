def solution(strlist):
    return list(map(lambda x: len(x), strlist))


solution_result = solution(["We", "are", "the", "world!"])
print(f'결과 = {solution_result}')
