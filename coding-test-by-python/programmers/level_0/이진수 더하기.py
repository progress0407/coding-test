# def solution(bin1, bin2):
#     answer = ''
#     bin1_power_arr = create_power_arr(bin1)
#     bin2_power_arr = create_power_arr(bin2)
#     print(f'bin1_power_arr = {bin1_power_arr}')
#     print(f'bin2_power_arr = {bin2_power_arr}')
#     bin1_sum = sum(bin1_power_arr)
#     bin2_sum = sum(bin2_power_arr)
#     tot = bin1_sum + bin2_sum
#     return answer


# def create_power_arr(bin1):
#     bin1_arr = [int(i) for i in list(bin1)]
#     bin1_size = len(bin1)
#     bin1_power_arr = [bin1_arr[i] * (2 ** (bin1_size - 1 - i)) for i in range(bin1_size)]
#     return bin1_power_arr


def solution(bin1, bin2):
    n1 = int('0b' + bin1, 2)
    n2 = int('0b' + bin2, 2)
    bin_sum = bin(n1 + n2)
    # return bin_sum.removeprefix('0b')
    # return bin_sum.replace('0b', '')
    return bin_sum[2:]


solution_result = solution("10", "11")
print(f'결과 = {solution_result}')
