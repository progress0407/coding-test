# def solution(my_string):
#     filtered = filter(lambda x: x in '0123456789', my_string)
#     mapped = list(map(lambda x: int(x), filtered))
#     return sum(mapped)

def solution(my_string):
    return sum([int(ch) for ch in my_string if ch.isdigit()])


solution_result = solution("aAb1B2cC34oOp")
print(f'결과 = solution_result')
