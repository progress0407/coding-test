def solution(sides):
    sides.sort()
    max_side = sides[-1]
    others_sum = sides[0] + sides[1]
    return 1 if max_side < others_sum else 2


if __name__ == '__main__':
    result = solution([1, 2, 3])
    print(f'결과: {result}')
