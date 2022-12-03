def solution(data):
    a, b, c = data[:3]
    last = data[-1]
    if a - b == b - c:
        d = data[1] - data[0]
        return data[-1] + d
    else:
        r = data[1] / data[0]
        return last * r


if __name__ == '__main__':
    # result = solution([1, 2, 3, 4])
    result = solution([2, 4, 8])
    print(f'결과: {result}')
