def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4


if __name__ == '__main__':
    result = solution(95)
    print(f'결과: {result}')

