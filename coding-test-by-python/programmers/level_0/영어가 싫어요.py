# def solution(input_string):
#     alphabet_to_number = {"zero": '0',
#                           "one": '1',
#                           "two": '2',
#                           "three": '3',
#                           "four": '4',
#                           "five": '5',
#                           "six": '6',
#                           "seven": '7',
#                           "eight": '8',
#                           "nine": '9'}
#
#     for alphabet in alphabet_to_number:
#         number = alphabet_to_number[alphabet]
#         input_string = input_string.replace(alphabet, number)
#     return int(input_string)


def solution(input_str):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        input_str = input_str.replace(eng, str(num))
    return int(input_str)


solution_result = solution('onetwothreefourfivesixseveneightnine')
print(f'결과 = {solution_result}')
