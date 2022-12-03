def solution(array, height):
    new_arr = []
    for e in array:
        if e > height:
            new_arr.append(e)
    return len(new_arr)


if __name__ == '__main__':
    result = solution2([149, 180, 192, 170], 167)
    print(f'결과: {result}')
