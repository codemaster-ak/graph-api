BASE_POINT_COLOR = '#1890ff'
BASE_CONNECTION_COLOR = '#656565'


def to_base_colours(matrix: list) -> list:
    mtx = matrix.copy()
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i == 0 and j > 0:
                col['colour'] = BASE_CONNECTION_COLOR
            if j == 0 and i > 0:
                col['colour'] = BASE_POINT_COLOR
    return mtx


def stack_to_base_colours(stack: list) -> list:
    stk = stack.copy()
    for shape in stk:
        if 'x' in shape and 'y' in shape:
            shape['colour'] = BASE_POINT_COLOR
        if 'from' in shape and 'to' in shape and 'weight' in shape:
            shape['colour'] = BASE_CONNECTION_COLOR
    return stk
