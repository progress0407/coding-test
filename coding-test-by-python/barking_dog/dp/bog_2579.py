def solution(s):
    length = len(s) - 1
    d = [[0 for c in range(2 + 1)] for r in range(length + 1)]
    d[1][1] = s[1]
    d[2][1] = s[2]
    d[2][2] = s[1] + s[2]

    for n in range(3, length + 1):
        d[n][1] = d[n - 1][2] + s[n]
        d[n][2] = max(d[n - 2][1], d[n - 2][2]) + s[n]
    return max(d[length])


tot_input = int(input())
input_list = [0]
for i in range(tot_input):
    input_list.append(int(input()))

solution_result = solution(input_list)
print(solution_result)
