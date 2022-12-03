# def solution(hp):
#     attacks = {5: 0, 3: 0, 1: 0}
#     for attack, count in attacks.items():
#         attacks[attack] = hp // attack
#         hp %= attack
#     return sum(attacks.values())

def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        num, hp = divmod(hp, ant)
        answer += num
    return answer


solution_result = solution(23)
print(f'결과 = {solution_result}')
