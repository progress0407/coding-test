def solution(target):
    result = list(filter(lambda x: target % x == 0, range(1, target + 1)))
    return len(result)


if __name__ == '__main__':
    solution_result = solution(20)
    print(f'정답: {solution_result}')
