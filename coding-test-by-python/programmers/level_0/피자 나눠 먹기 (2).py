import math

# def solution(i_n):
#     i_x = 6
#     x = i_x
#     y = i_n
#     while y != 0:
        # print(f'x,y = {x, y}')
        # x, y = y, x % y
    # gcm = x
    # lcm = gcm * (i_x // gcm) * (i_n // gcm)
    # 쳐먹어야할_피자_갯수 = lcm // 6
    # return 쳐먹어야할_피자_갯수


def solution(i_n):
    gcd = math.gcd(i_n, 6)
    print(f'gcd = {gcd}')
    lcm = (i_n * 6) // gcd
    return lcm


solution_result = solution(10)
print(f'결과 = {solution_result}')
