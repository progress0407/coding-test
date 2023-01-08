def solution(num, total):
    mid = total // num
    if num % 2 == 1:  # 홀
        length = (num - 1) // 2
        # return [n for n in range(mid - length, mid + length + 1)]
        return list(range(mid - length, mid + length + 1))
    else:  # 짝
        length = num // 2
        # return [n for n in range(mid - length + 1, mid + length + 1)]
        return list(range(mid - length + 1, mid + length + 1))


print(f'결과: {solution(3, 12)}')  # [3,4,5]
print(f'결과: {solution(5, 15)}')  # [1,2,3,4,5]
print(f'결과: {solution(4, 14)}')  # [2,3,4,5]
print(f'결과: {solution(5, 5)}')  # [-1,0,1,2,3]
