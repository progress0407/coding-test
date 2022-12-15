# def solution(commands):
#     commands = commands.split()
#     last = ''
#     summation = 0
#     for command in commands:
#         if command == 'Z':
#             summation -= int(last)
#         else:
#             summation += int(command)
#         last = command
#     return summation


# stack의 특성을 이용한 풀이
def solution(commands):
    commands = commands.split()
    numbers = []
    for command in commands:
        if command == 'Z':
            numbers.pop()
        else:
            numbers.append(int(command))
    return sum(numbers)


print(f'결과 = {solution("1 2 Z 3")}')  # 4
print(f'결과 = {solution("10 20 30 40")}')  # 100
print(f'결과 = {solution("10 Z 20 Z 1")}')  # 0
print(f'결과 = {solution("10 Z 20 Z")}')  # 1
print(f'결과 = {solution("-1 -2 -3 Z")}')  # -3
