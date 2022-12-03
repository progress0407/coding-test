def solution(money):
    return divmod(money, 5_500)


if __name__ == '__main__':
    result = solution(5_500)
    print(f'결과: {result}')
