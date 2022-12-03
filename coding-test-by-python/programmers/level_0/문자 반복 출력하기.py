def solution(my_string, n):
    return ''.join((map(lambda x: x * n, my_string)))


if __name__ == '__main__':
    result = solution([1, 2, 3])
    print(f'결과: {result}')
