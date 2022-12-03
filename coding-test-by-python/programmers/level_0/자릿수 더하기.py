def solution(n):
    return sum(list(map(int, list(str(n)))))
    # return sum([int(ch) for ch in str(n)])


if __name__ == '__main__':
    solution_result = solution(1234)
    print(f'정답: {solution_result}')
