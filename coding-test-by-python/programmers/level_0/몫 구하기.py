def solution(num1, num2):
    # num1 // num2
    return divmod(num1, num2)[0]


if __name__ == '__main__':
    result = solution(3, 2)
    print(f'결과: {result}')
