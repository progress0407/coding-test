# dp[2] : 1개
# 1+1

# dp[3] : 3개
# 1+2, 1+(1+1): (dp[2]+1)
# 2+1

# dp[4]: 7개
# 1+(1+1+1), 1+(1+2), 1+(2+1), 1+(3): dp[3]+1
# 2+(1+1), 2+(2): dp[2]+1
# 3+(1): 1

# dp[5]: 1+1+2+3+7 = 1 + dp[1..4]
# 5
# 4 + dp[1]


def solution(input_number):
    dp = {2: 1}
    for n in range(3, input_number + 1):
        dp[n] = sum(dp.values()) + (n - 1)
    print(dp)
    return dp[input_number]


solution_result = solution(int(input()))
print(solution_result)
