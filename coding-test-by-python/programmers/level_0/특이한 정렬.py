# 정렬 조건!
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(n - x), -x))


print(f'결과: {solution([1, 2, 3, 4, 5, 6], 4)}')
