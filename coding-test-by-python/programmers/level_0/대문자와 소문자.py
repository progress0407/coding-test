# def solution(my_string):
#     result = []
#     for ch in my_string:
#         if ch.isupper():
#             result.append(ch.lower())
#         else:
#             result.append(ch.upper())
#     return ''.join(result)


# def solution(my_string):
#     result = ''
#     for ch in my_string:
#         if ch.isupper():
#             result += ch.lower()
#         else:
#             result += ch.upper()
#     return ''.join(result)


def solution(my_string):
    return my_string.swapcase()


solution_result = solution("cccCCC")
print(f'결과 = {solution_result}')
