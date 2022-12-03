def solution(my_string):
    digit = sorted([int(ch) for ch in my_string if ch.isdigit()])
    # digit.sort()
    return digit


solution_result = solution("hi12392")
print(f'결과 = {solution_result}')
