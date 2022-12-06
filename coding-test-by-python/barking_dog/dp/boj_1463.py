# 1로 만들기

def solution(input_number):
    dp = {1: 0, 2: 1, 3: 1}
    for n in range(4, input_number + 1):
        candidate = [dp[n - 1]]
        if n % 3 == 0:
            candidate.append(dp[n // 3])
        if n % 2 == 0:
            candidate.append(dp[n // 2])
        dp[n] = min(candidate) + 1
    return dp[n]


input_number = int(input())
solution_result = solution(input_number)
print(solution_result)
