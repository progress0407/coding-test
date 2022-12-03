def solution(numbers):
    # return list(map(lambda x: x * 2, numbers))
    return [n * 2 for n in numbers]


if __name__ == '__main__':
    result = solution([1, 2, 3, 4, 5])
    print(f'결과: {result}')
