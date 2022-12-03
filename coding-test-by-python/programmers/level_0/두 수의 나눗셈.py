def solution(num1, num2):
    return int((num1/ num2) * 1_000)


if __name__ == '__main__':
    # result = solution(3, 2)
    result = solution(7, 3)
    # result = solution(1, 16)
    print(f'결과: {result}')
