# def solution(dots):
#     dots.sort()
#     x1 = dots[0][0]
#     x2 = dots[2][0]
#     y1 = dots[0][1]
#     y2 = dots[1][1]
#
#     dx = abs(x1 - x2)
#     dy = abs(y1 - y2)
#     sector = dx * dy
#
#     return sector


def solution(dots):
    max_dot = max(dots)
    min_dot = min(dots)

    dx = abs(max_dot[0] - min_dot[0])
    dy = abs(max_dot[1] - min_dot[1])
    sector = dx * dy

    return sector


print(f'결과 = {solution([[1, 1], [2, 1], [2, 2], [1, 2]])}')
