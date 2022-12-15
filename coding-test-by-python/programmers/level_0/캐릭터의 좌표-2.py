def solution(keyinput, board):
    op_to_dir = {
        "up": Coord(0, +1),
        "down": Coord(0, -1),
        "left": Coord(-1, 0),
        "right": Coord(+1, 0)
    }
    cur_pos = Coord(0, 0)
    lim_x, lim_y = (board[0] - 1) // 2, (board[1] - 1) // 2
    for key in keyinput:
        d = op_to_dir[key]
        moved = cur_pos.add(d)
        if validate_pos(lim_x, lim_y, moved):
            continue
        cur_pos.move(d)

    return cur_pos.display()


class Coord:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, coord):
        return Coord(self.x + coord.x, self.y + coord.y)

    def move(self, coord):
        self.x += coord.x
        self.y += coord.y

    # for view
    def display(self):
        return [self.x, self.y]


def validate_pos(lim_x, lim_y, moved):
    return abs(moved.x) > lim_x or abs(moved.y) > lim_y


solution_result = solution(["left", "right", "up", "right", "right"], [11, 11])
print(f'결과 = {solution_result}')
