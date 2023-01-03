# fail

def solution(polynomial):
    trans_polynomial = polynomial.split(" + ")
    tot_x = 0
    tot_num = 0
    for num_str in trans_polynomial:
        if num_str.count('x') > 0:
            x_num = create_x_num(num_str)
            tot_x += x_num
        else:
            const_num = int(num_str)
            tot_num += const_num
    return print_polynomial(tot_num, tot_x)


# def create_x_num(num_str):
#     try:
#         return int(num_str.split("x")[0])
#     except ValueError:  # x 인 경우
#         return 1

def create_x_num(num_str):
    if num_str == 'x':
        return 1
    return int(num_str.split("x")[0])


def print_polynomial(tot_num, tot_x):
    if tot_x == 0:
        return f'{tot_num}'
    elif tot_num == 0:
        return f'{tot_x}x'
    else:
        return f'{tot_x}x + {tot_num}'


# print(f'결과: {solution("3x + 7 + x")}')  # "4x + 7"
# print(f'결과: {solution("x + x + x")}')  # "3x"
# print(f'결과: {solution("1 + 2 + 3")}')  # "6"
# print(f'결과: {solution("0 + 1 + 1")}')  # "2"
# print(f'결과: {solution("0x + 1 + 1")}')  # "2"
# print(f'결과: {solution("0 + 0")}')  # "2"
print(f'결과: {solution("0 + 11 + 2x + 5x")}')  # "7x + 11"
