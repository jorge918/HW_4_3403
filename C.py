#region imports
import numpy as np
#endregion

def main():
    """
    Main function to demonstrate solving linear systems using numpy.
    """
    # Define coefficient matrices A1 and A2, and vectors b1 and b2
    A1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
    A2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
    b1 = np.array([2, 12, 10])
    b2 = np.array([2, 12, 21, 37])

    # Solve linear system Ax = b for x using numpy's linalg.solve
    x1 = np.linalg.solve(A1, b1)
    x2 = np.linalg.solve(A2, b2)

    # Print the solutions and verify the results
    print("x1^T = ", x1)
    print("b = ", np.matmul(A1, x1))  # Verify solution by multiplying A1 by x1
    print("x2^T = ", x2)
    print("b = ", np.matmul(A2, x2))  # Verify solution by multiplying A2 by x2

if __name__ == "__main__":
    main()
