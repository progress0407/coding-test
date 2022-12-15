# def solution(spell, dic):
#     spell = ''.join(sorted(spell))
#     print(spell)
#     dic = [''.join(sorted(w)) for w in dic]
#     print(dic)
#     for w in dic:
#         if spell == w:
#             return 1
#     return 2


# 집합의 특성 이용
def solution(spell, dic):
    spell = set(spell)
    for w in dic:
        # if not spell - set(w):
        if spell == set(w):
            return 1
    return 2


# solution_result = solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])
solution_result = solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])
print(f'결과 = {solution_result}')
