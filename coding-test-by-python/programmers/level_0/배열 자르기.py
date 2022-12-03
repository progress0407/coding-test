def solution(numbers, num1, num2):
    return numbers[num1:num2 + 1]


if __name__ == '__main__':
    result = solution([1, 2, 3, 4, 5], 1, 3)
    print(f'결과: {result}')
