import math


def solution(denum1, num1, denum2, num2):
    gcd = math.gcd(num1, num2)
    lcm = (num1 * num2) // gcd

    one_multiplier = lcm // num1
    other_multiplier = lcm // num2

    num1_multiplied = num1 * one_multiplier
    denum1_multiplied = denum1 * one_multiplier

    num2_multiplied = num2 * other_multiplier
    denum2_multiplied = denum2 * other_multiplier

    denum = denum1_multiplied + denum2_multiplied
    num = num1_multiplied

    lcm_between_denum_num = math.gcd(denum, num)

    return [denum // lcm_between_denum_num, num // lcm_between_denum_num]


print(f'결과: {solution(1, 2, 3, 4)}')  # [5,4]
