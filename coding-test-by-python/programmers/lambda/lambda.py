from functools import reduce


def learn_map():
    new_list = list(map(lambda x: x ** 2, range(5)))
    print(new_list)
    print(list(range(5)))
    print([range(5)])


def learn_reduce():
    # result = reduce(lambda x, y: x + y, range(5))  # 0~4 합
    # result = reduce(lambda x, y: x + y, 'abcde')
    result = reduce(lambda x, y: x + y, ['a', 'b', 'c'])
    print(result)


def learn_filter():
    # result = list(filter(lambda x: x < 5, range(10)))
    # 1 == True, 0 == False
    # 홀수만 추려내자
    # result = list(filter(lambda x: x % 2, range(10)))
    result = list(filter(lambda x: x % 2 == 0, range(10)))
    print(result)


if __name__ == '__main__':
    # learn_map()
    # learn_reduce()
    learn_filter()
