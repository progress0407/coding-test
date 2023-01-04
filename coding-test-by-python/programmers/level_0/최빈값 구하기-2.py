def solution(array):
    print(f'set={set(array)}')
    while len(array) != 0:
        en = enumerate(set(array))
        for i, a in en:
            print(f'i = {i}, a = {a}')
            array.remove(a)
        if i == 0: return a
    return -1


print(f'결과: {solution([1, 2, 3, 3, 3, 4])}')  # 3
# print(f'결과: {solution([1, 1, 2, 2])}')  # -1
# print(f'결과: {solution([1, 1, 1])}')  # 1
# print(f'결과: {solution([1])}')  # 1
