def solution(str1, str2):
    if str2 in str1:
        return 1
    return 2


if __name__ == '__main__':
    solution_result = solution('ab6CDE443fgh22iJKlmn1o', '6CD')
    print(f'정답: {solution_result}')
