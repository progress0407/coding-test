def solution(my_string):
    new_list = []
    for c in my_string:
        # if new_list.count(c) == 0:
        if c not in new_list:
            new_list.append(c)
    return ''.join(new_list)


solution_result = solution('people')
print(f'결과 = {solution_result}')
