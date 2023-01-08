# (x, y) = (c, r)
dir_vectors = [
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0)
]
r_max = 0
c_max = 0


def solution(board):
    global r_max
    r_max = len(board)
    global c_max
    c_max = len(board[0])

    dot_list = []
    for r, record in enumerate(board):
        for c, dot in enumerate(record):
            if dot == 1:
                dot_list.append((c, r))

    for dot in dot_list:
        check_emergency_area(board, dot)

    tot_dot_cnt = r_max * c_max
    emergency_cnt = 0
    for record in board:
        for dot in record:
            if dot == 1:
                emergency_cnt += 1
    return tot_dot_cnt - emergency_cnt


def check_emergency_area(board, dot):
    c = dot[0]
    r = dot[1]
    for dir in dir_vectors:
        if not (0 <= c + dir[0] < c_max) or not (0 <= r + dir[1] < r_max):
            continue
        d_c, d_r = move_point(dir, (c, r))
        board[d_r][d_c] = 1


def move_point(dir_vector, point):
    return point[0] + dir_vector[0], point[1] + dir_vector[1]


print(f'결과: {solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])}')  # 16
