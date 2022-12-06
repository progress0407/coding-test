def solution(i, j, k):
    return sum(str(n).count(str(k)) for n in range(i, j + 1))


solution_result = solution(1, 13, 1)
print(solution_result)
