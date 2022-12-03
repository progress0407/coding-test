def solution(my_string, letter):
    return my_string.replace(letter, '')


if __name__ == '__main__':
    result = solution("abcdef", "f")
    print(f'결과: {result}')

