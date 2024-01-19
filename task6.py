import numpy as np

def solve_linear_system(A, b):
    x = np.linalg.solve(A, b)
    return x

A = np.array([[1, 2, 3],
              [2, 5, 3],
              [2, 0, 8]])

b = np.array([10, 15, 20])

solution = solve_linear_system(A, b)

print("Solution vector x:")
print(solution)

