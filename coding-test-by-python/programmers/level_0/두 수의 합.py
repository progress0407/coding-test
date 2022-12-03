# solution = lambda a, b: a + b
solution = lambda *x: sum(x)

if __name__ == '__main__':
    result = solution(3, 2, 1)
    print(f'결과: {result}')
