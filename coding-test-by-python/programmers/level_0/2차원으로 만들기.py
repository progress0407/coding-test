# def solution(num_list, n):
#     result = []
#     for k in range(0, len(num_list), n):
#         add_list = [num_list[l] for l in range(k, k + n)]
#         result.append(add_list)
#     return result


def solution(num_list, n):
    return [num_list[x:x + n] for x in range(0, len(num_list), n)]


solution_result = solution([1, 2, 3, 4, 5, 6, 7, 8], 2)
print(solution_result)
