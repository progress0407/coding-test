# def solution(num_list):
#     new_arr = []
#     for e in reversed(num_list):
#         new_arr.append(e)
#     return new_arr


# 새로운 배열을 생성
# def solution(num_list):
#     return num_list[::-1]


def solution(num_list):
    num_list.reverse()
    return num_list


if __name__ == '__main__':
    result = solution([1, 2, 3, 4, 5])
    print(f'결과: {result}')
