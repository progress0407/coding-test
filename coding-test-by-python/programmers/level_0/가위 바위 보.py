def solution(rsp):
    win_fn = {'2': '0', '0': '5', '5': '2'}
    # win_cases = [win_fn.get(i) for i in rsp]
    win_cases = [win_fn[i] for i in rsp]
    return ''.join(win_cases)


solution_result = solution("205")
print(f'결과 = {solution_result}')
