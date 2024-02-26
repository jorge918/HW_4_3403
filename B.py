#region imports
import math
from math import cos
from scipy.optimize import fsolve
import numpy as np
#endregion


def main():
    """
    Main function to demonstrate the use of fsolve to find roots of functions.
    """
    # Define the first function fn1(x) = x - 3*cos(x)
    fn1 = lambda x: x - 3 * cos(x)

    # Define the second function fn2(x) = cos(2*x) * x^3
    fn2 = lambda x: cos(2 * x) * x ** 3

    # Maximum number of iterations for each fsolve call
    maxiter1 = 5
    maxiter2 = 15
    maxiter3 = 3

    # Find the root of fn1 with fsolve, starting from x=1
    r1 = fsolve(fn1, 1, xtol=1E-4, maxfev=maxiter1)[0]

    # Find the root of fn2 with fsolve, starting from x=1
    r2 = fsolve(fn2, 1, xtol=1E-8, maxfev=maxiter2)[0]

    # Find another root of fn2 with fsolve, starting from x=1
    r3 = fsolve(fn2, 1, xtol=1E-8, maxfev=maxiter3)[0]

    # Print the results
    print("r1={:.6}".format(r1))
    print("fn1(r1)={:0.6}".format(fn1(r1)))
    print("\nwith maxiter={}: r2={:0.6f}".format(maxiter2, r2))
    print("fn2(r2)={:0.6f}".format(fn2(r2)))
    print("\nwith maxiter={}: r3={:0.6f}".format(maxiter3, r3))
    print("fn2(r3)={:0.6f}".format(fn2(r3)))


if __name__ == "__main__":
    main()
