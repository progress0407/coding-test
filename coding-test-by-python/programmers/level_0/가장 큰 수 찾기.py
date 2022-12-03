def solution(array):
    max_number = max(array)
    max_number_index = array.index(max_number)
    return [max_number, max_number_index]


solution_result = solution([1, 8, 3])
print(f'결과 = {solution_result}')
