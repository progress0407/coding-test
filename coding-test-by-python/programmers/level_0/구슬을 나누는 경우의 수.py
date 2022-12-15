from math import comb


# def solution(balls, share):
#     return factorial(balls) // (factorial(share) * factorial(balls - share))


def solution(balls, share):
    return comb(balls, share)


# solution_result = solution(3, 2)
solution_result = solution(5, 3)
print(f'결과 = {solution_result}')
