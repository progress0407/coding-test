# Split

def solution(quiz):
    answer_list = []
    for stmt in quiz:
        L, R = stmt.split(' = ')
        a, op, b = L.split()
        a = int(a)
        b = int(b)
        R = int(R)
        answer_list.append(score(a, op, b, R))

    return answer_list


def score(a, op, b, R):
    if op == '+':
        if a + b == R:
            return 'O'
        else:
            return 'X'
    elif op == '-':
        if a - b == R:
            return 'O'
        else:
            return 'X'


print(f'결과: {solution(["3 - 4 = -3", "5 + 6 = 11"])}')  # 3
