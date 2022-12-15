def solution(n):
    result = []
    while n != 1:
        for x in range(2, n + 1):
            if n % x == 0:
                result.append(x)
                n //= x
                break
    return list(set(result))


# solution_result = solution(12)
# solution_result = solution(420)
# solution_result = solution(2)
solution_result = solution(16)
print(f'결과 = {solution_result}')
