def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]


if __name__ == '__main__':
    result = solution([1, 2, 3, 4, 5])
    print(f'결과: {result}')