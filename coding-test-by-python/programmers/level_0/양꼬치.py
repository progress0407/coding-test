def solution(양꼬치, 음료):
    service = 양꼬치 // 10
    음료 = max(0, 음료 - service)
    return 12_000 * 양꼬치 + 2_000 * 음료


if __name__ == '__main__':
    # result = solution(10, 3)
    result = solution(64, 6)
    print(f'결과: {result}')
