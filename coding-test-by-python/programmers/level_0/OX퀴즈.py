def solution(quiz):
    answer_list = []
    for stmt in quiz:
        split_str = stmt.split(' = ')
        left_exp = split_str[0]
        right_exp = int(split_str[1])
        left_terms = left_exp.split(' ')
        while len(left_terms) != 1:
            left = int(left_terms.pop(0))
            op = left_terms.pop(0)
            right = int(left_terms.pop(0))
            result = calc(left, op, right)
            left_terms.insert(0, result)

        right_answer = left_terms.pop(0)
        answer_list.append(judge(right_answer, right_exp))

    return answer_list


def judge(right_answer, right_exp):
    if right_exp == right_answer:
        return 'O'
    else:
        return 'X'


def calc(left, op, right):
    if op == '-':
        return left - right
    elif op == '+':
        return left + right



print(f'결과: {solution(["3 - 4 = -3", "5 + 6 = 11"])}')  # 3