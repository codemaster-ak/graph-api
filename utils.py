BASE_POINT_COLOR = '#1890ff'
BASE_CONNECTION_COLOR = '#656565'


def to_base_colours(matrix: list):
    mtx = matrix.copy()
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i == 0 and j > 0:
                col['colour'] = BASE_CONNECTION_COLOR
            if j == 0 and i > 0:
                col['colour'] = BASE_POINT_COLOR
    return mtx
