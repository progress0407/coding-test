# def solution(cipher, code):
#     start = code - 1
#     end = len(cipher)
#     step = code
#     ch_list = [cipher[i] for i in range(start, end, step)]
#     return ''.join(ch_list)


def solution(cipher, code):
    return cipher[code-1::code]


solution_result = solution('dfjardstddetckdaccccdegk', 4)
print(f'결과 = {solution_result}')
