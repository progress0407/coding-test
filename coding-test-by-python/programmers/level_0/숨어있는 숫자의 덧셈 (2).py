import re
# fail
# def solution(my_string):
#     return sum([int(i) for i in my_string if i.isdigit()])


# def solution(my_string):
#     result = re.split(r'[a-zA-Z]', my_string)
#     result = [int(n) for n in result if n.isdigit()]
#     return sum(result)


def solution(my_string):
    result = ''.join(i if i.isdigit() else ' ' for i in my_string)
    result = [int(n) for n in result.split()]
    return sum(result)


solution_result = solution("aAb1B2cC34oOp")
print(f'결과 = {solution_result}')
