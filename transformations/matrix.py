import math
from typing import List, Tuple

Matrix3x3 = List[List[float]]
Point2D   = Tuple[float, float] 

def identity_matrix() -> Matrix3x3:
    return [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]


def multiply_matrix(matrix_a: Matrix3x3, matrix_b: Matrix3x3) -> Matrix3x3:
    result: Matrix3x3 = [[0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0]]
 
    for i in range(3):          # row of A
        for j in range(3):      # column of B
            total = 0.0
            for k in range(3):  # shared dimension
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
 
    return result


def multiply_point(matrix: Matrix3x3, point: Point2D) -> Point2D:
    x, y = point

    x_h = matrix[0][0] * x + matrix[0][1] * y + matrix[0][2] * 1.0
    y_h = matrix[1][0] * x + matrix[1][1] * y + matrix[1][2] * 1.0
    w_h = matrix[2][0] * x + matrix[2][1] * y + matrix[2][2] * 1.0

    return (x_h / w_h, y_h / w_h)


def translation_matrix(tx: float, ty: float) -> Matrix3x3:
    return [
        [1.0, 0.0, tx],
        [0.0, 1.0, ty],
        [0.0, 0.0, 1.0],
    ]

def rotation_matrix(angle: float) -> Matrix3x3:
    theta = math.radians(angle)
 
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
 
    return [
        [cos_t, -sin_t, 0.0],
        [sin_t,  cos_t, 0.0],
        [0.0,    0.0,   1.0],
    ]

def scaling_matrix(sx: float, sy: float) -> Matrix3x3:
    return [
        [sx,  0.0, 0.0],
        [0.0, sy,  0.0],
        [0.0, 0.0, 1.0],
    ]

