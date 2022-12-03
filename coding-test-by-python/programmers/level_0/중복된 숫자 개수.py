def solution(array, n):
    return array.count(n)


if __name__ == '__main__':
    result = solution([1, 1, 2, 3, 4, 5], 1)
    print(f'결과: {result}')
