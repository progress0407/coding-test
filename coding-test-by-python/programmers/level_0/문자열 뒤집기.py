# def solution(my_string):
#     arr = []
#     for e in reversed(my_string):
#         arr.append(e)
#     return ''.join(arr)


def solution(my_string):
    return my_string[::-1]


if __name__ == '__main__':
    result = solution("jaron")
    print(f'결과: {result}')
