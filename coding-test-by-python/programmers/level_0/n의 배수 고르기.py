def solution(n, numlist):
    numbers = [int(ch) for ch in numlist]
    return [i for i in numbers if i % n == 0]


solution_result = solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f'결과 = {solution_result}')
