# -3 -2 0 2 3
# -3 0 2 3
# -3 2 3 4
# -3 -2 0 2 3
# -4 -1 0 2 3
# -4 -1 0 3
# a b c d e

# k = max(a*b, d*e)
# k > max(b*c, c*d) > ...


# def solution(numbers):
#     target_list = []
#     for i in numbers:
#         target_list += [i * j for j in numbers if i is not j]
#     return max(target_list)


def solution(numbers):
    target_list = []



solution_result = solution([1, 2, -3, 4, -5])
print(f'결과 = {solution_result}')
