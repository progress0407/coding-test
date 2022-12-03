def solution(dot):
    x = dot[0]
    y = dot[1]
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


if __name__ == '__main__':
    result = solution([2, 4])
    print(f'결과: {result}')
