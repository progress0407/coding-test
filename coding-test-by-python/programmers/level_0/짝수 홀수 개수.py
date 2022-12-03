# def solution(num_list):
#     even = []
#     for n in num_list:
#         if n % 2 == 0:
#             even.append(n)
#     return [len(even), len(num_list) - len(even)]


def solution(num_list):
    evens_and_odds = list(map(lambda x: x % 2, num_list))
    even = evens_and_odds.count(0)
    odd = evens_and_odds.count(1)
    return [even, odd]


if __name__ == '__main__':
    result = solution([1, 2, 3, 4, 5])
    print(f'결과: {result}')
