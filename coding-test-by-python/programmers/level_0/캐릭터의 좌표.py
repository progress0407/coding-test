def solution(keyinput, board):
    op_to_dir = {
        "up": [0, +1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [+1, 0]
    }
    cur_pos = [0, 0]
    lim_x, lim_y = (board[0] - 1) // 2, (board[1] - 1) // 2
    for key in keyinput:
        d = op_to_dir[key]
        moved_x, moved_y = moved_pos(cur_pos, d)
        if validate_pos(lim_x, lim_y, moved_x, moved_y):
            continue
        cur_pos[0], cur_pos[1] = moved_x, moved_y

    return cur_pos


def moved_pos(cur_pos, d):
    return cur_pos[0] + d[0], cur_pos[1] + d[1]


def validate_pos(lim_x, lim_y, moved_x, moved_y):
    return abs(moved_x) > lim_x or abs(moved_y) > lim_y


solution_result = solution(["left", "right", "up", "right", "right"], [11, 11])
print(f'결과 = {solution_result}')
