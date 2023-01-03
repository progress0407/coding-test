def solution(chicken):
    service_count = 0
    while chicken >= 10:
        coupon, remainder = divmod(chicken, 10)
        service_count += coupon
        chicken = coupon + remainder
    return service_count


# print(f'결과: {solution(100)}')
print(f'결과: {solution(1081)}')
