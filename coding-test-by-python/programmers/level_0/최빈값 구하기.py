def solution(array):
    dict = create_dict(array)

    sorted_dict = sorted(dict.items(), key=lambda item: item[1])  # item[1] == value
    print(f'sorted_dict = {sorted_dict}')

    if len(sorted_dict) == 1:
        return sorted_dict.pop()[0]

    first = sorted_dict.pop()
    second = sorted_dict.pop()

    if first[1] == second[1]:
        return -1
    return first[0]


def create_dict(array):
    dict = {}
    for n in set(array):
        dict[n] = array.count(n)
    return dict


print(f'결과: {solution([1, 2, 3, 3, 3, 4])}')  # 3
print(f'결과: {solution([1, 1, 2, 2])}')  # -1
print(f'결과: {solution([1, 1, 1])}')  # 1
print(f'결과: {solution([1])}')  # 1
