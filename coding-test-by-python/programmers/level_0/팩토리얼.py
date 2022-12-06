# def solution(upper_bound):
#     n = 1
#     factorial_number = 1
#     limit_number = 3_628_800
#     while n <= limit_number:
#         if factorial_number == upper_bound:
#             return n
#         elif factorial_number > upper_bound:
#             return n - 1
#         else:
#             n += 1
#             factorial_number *= n

def solution(upper_bound):
    n, k = 1, 1
    while n <= upper_bound:
        k += 1
        n *= k
    return k - 1


solution_result = solution(3628800)
print(solution_result)
