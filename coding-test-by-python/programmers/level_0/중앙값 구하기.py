def solution(array):
    array.sort()
    length = len(array)
    return array[int(length / 2)]


if __name__ == '__main__':
    solution_result = solution([1, 2, 7, 10, 11])
    print(f'정답: {solution_result}')
