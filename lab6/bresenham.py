"""
    Bresenham algorithms
"""


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def bresenham_int(start_point, end_point, color):
    """
        Implementation of Bresenham line drawing algorithm.
    """

    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]

    if dx == 0 and dy == 0:
        return [[start_point[0], start_point[1], color]]

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    two_dy = 2 * dy
    two_dx = 2 * dx

    e = two_dy - dx

    x = start_point[0]
    y = start_point[1]
    points = []

    i = 0
    while i <= dx:
        points.append([x, y, color])

        if e >= 0:
            if exchange == 1:
                x += x_sign
            else:
                y += y_sign

            e -= two_dx

        if exchange == 1:
            y += y_sign
        else:
            x += x_sign

        e += two_dy
        i += 1

    return points
