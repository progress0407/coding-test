def solution(n):
    return list(filter(lambda x: x % 2 == 1, range(n + 1)))


if __name__ == '__main__':
    result = solution(15)
    print(f'결과: {result}')
