# def solution(array):
#     sub_array = lambda e: list(map(lambda x: int(x), list(str(e))))
#     seven_count = [sub_array(e).count(7) for e in array]
#     return sum(seven_count)


def solution(array):
    str_all_combined = ''.join(list(map(str, array)))
    return str_all_combined.count('7')


solution_result = solution([7, 77, 17])
print(solution_result)
