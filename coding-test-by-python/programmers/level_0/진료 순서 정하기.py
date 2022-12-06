# def solution(emergency):
#     sorted_emergency = sorted(emergency, reverse=True)
#     result = {x: 0 for x in emergency}
#     rank = 1
#     for e in sorted_emergency:
#         result[e] = rank
#         rank += 1
#     return list(result.values())


def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(i) + 1 for i in emergency]


solution_result = solution([3, 76, 24])
print(solution_result)
