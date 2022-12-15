def solution(M, N):
    col_count = M - 1
    row_count = (N - 1) * M
    return col_count + row_count


solution_result = solution(2, 2)
print(f'결과 = {solution_result}')
