# def solution(price):
#     if price >= 500_000:
#         return int(price * 0.80)
#     elif price >= 300_000:
#         return int(price * 0.90)
#     elif price >= 100_000:
#         return int(price * 0.95)
#     else:
#         return price


def solution(price):
    discount_rates = {500_000: 0.8, 300_000: 0.9, 100_000: 0.95, 0: 1}
    for discount_pivot_price, discount_rate in discount_rates.items():
        if price >= discount_pivot_price:
            return int(price * discount_rate)


if __name__ == '__main__':
    solution_result = solution(100_000)
    print(f'정답: {solution_result}')
