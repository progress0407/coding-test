def solution(my_string, num1, num2):
    number_list = list(my_string)
    swap(number_list, num1, num2)
    return ''.join(number_list)


def swap(number_list, num1, num2):
    number_list[num1], number_list[num2] = number_list[num2], number_list[num1]


solution_result = solution("hello", 1, 2)
print(f'결과 = {solution_result}')
