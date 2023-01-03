def solution(dest_num):
    trans_num = 0
    for num in range(1, dest_num + 1):

        trans_num += 1
        while is_3_multiple(trans_num) or does_contain_3(trans_num):
            trans_num += 1
        print(f'num = {num}, t_num = {trans_num}')
    return trans_num


def is_3_multiple(trans_num):
    return trans_num % 3 == 0


def does_contain_3(trans_num):
    return str(trans_num).count('3') > 0


print(f'결과: {solution(10)}')  # 16
