"""
    function returns a list of lists of integers representing the Pascal’s triangle of n
    Returns an empty list if n <= 0
"""

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if n <= 0:
            return []
        else:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle


