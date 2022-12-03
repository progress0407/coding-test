def solution(n):
    # arr = [num for num in range(0, n + 1) if num % 2 == 0]
    arr = [num for num in range(0, n + 1, 2)]
    return sum(arr)


if __name__ == '__main__':
    result = solution(10)
    print(f'결과: {result}')
