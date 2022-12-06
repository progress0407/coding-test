def solution(s):
    s = list(s)
    symbol = set(s)
    dict = {e: s.count(e) for e in symbol if s.count(e) == 1}
    only_one_characters = sorted(list(dict.keys()))
    return ''.join(only_one_characters)


# solution_result = solution("abcabcadc")
# solution_result = solution("abdc")
solution_result = solution("hello")
print(solution_result)
