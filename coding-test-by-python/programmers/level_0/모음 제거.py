# def solution(my_string):
#     vowels = ('a', 'e', 'i', 'o', 'u')
#
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     return my_string

def solution(my_string):
    return ''.join([ch for ch in my_string if not (ch in "aeiou")])


solution_result = solution("bus")
print(solution_result)
