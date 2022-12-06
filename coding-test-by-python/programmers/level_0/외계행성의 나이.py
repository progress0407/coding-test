# def solution(age):
#     age_translater = {
#         '0': 'a',
#         '1': 'b',
#         '2': 'c',
#         '3': 'd',
#         '4': 'e',
#         '5': 'f',
#         '6': 'g',
#         '7': 'h',
#         '8': 'i',
#         '9': 'j'
#     }
#     age_arr = list(str(age))
#     new_age_arr = [age_translater[i] for i in age_arr]
#     return ''.join(new_age_arr)


def solution(age):
    function = lambda x: chr(int(x) + 97)
    new_age_list = [function(i) for i in str(age)]
    return ''.join(new_age_list)


solution_result = solution(23)
print(f'결과 = {solution_result}')
