# def solution(s1, s2):
#     count = 0
#     for a in s1:
#         if s2.count(a):
#             count += 1
#     return count


def solution(s1, s2):
    return len(set(s1) & set(s2))


if __name__ == '__main__':
    solution_result = solution(["a", "b", "c"], ["com", "b", "d", "p", "c"])
    print(f'정답: {solution_result}')
