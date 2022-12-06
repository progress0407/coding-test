# def solution(order):
#     match_list = [3, 6, 9]
#     target_list = list(map(lambda x: int(x), list(str(order))))
#     match_count_list = [target_list.count(n) for n in match_list]
#     return sum(match_count_list)


# 내 풀이가 likes1 보다 간단함!

def solution(order):
    return sum([str(order).count(n) for n in ['3', '6', '9']])


solution_result = solution(29423)
print(f'결과 = {solution_result}')
