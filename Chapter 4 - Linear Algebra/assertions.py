# assertions.py

from vector import (add, subtract, vector_sum, scalar_multiply, 
                        vector_mean, dot, sum_of_squares, magnitude,distance)

from matrices import shape, identity_matrix, get_column, get_row, make_matrix


# Vector
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9] 
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4] 
assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6
assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3
assert magnitude([3, 4]) == 5

# Matrices
assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns
assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]




