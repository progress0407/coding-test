def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)


def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]


print(f'결과: {solution(["3 - 4 = -3", "5 + 6 = 11"])}')  # 3
