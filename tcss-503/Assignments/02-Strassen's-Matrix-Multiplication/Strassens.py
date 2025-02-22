import numpy as np

def recursive_matrix_mult(A, B):
    """
    Recursively multiplies sub matrices of A and B
    :param a: The first Matrix A implemented as a np.array
    :param b: The second Matrix B implemented as a np.array
    :return: The product of a and b
    """
    a = np.array(A)
    b = np.array(B)
    if len(a) == 1:
        return a*b

    n = a.shape[0] // 2
    a0 = a[:n, :n]  # UPPER LEFT
    a1 = a[:n, n:]  # UPPER RIGHT
    a2 = a[n:, :n]  # LOWER LEFT
    a3 = a[n:, n:]  # LOWER RIGHT

    b0 = b[:n, :n]  # UPPER LEFT
    b1 = b[:n, n:]  # UPPER RIGHT
    b2 = b[n:, :n]  # LOWER LEFT
    b3 = b[n:, n:]  # LOWER RIGHT

    c0 = recursive_matrix_mult(a0, b0) + recursive_matrix_mult(a1, b2)
    c1 = recursive_matrix_mult(a0, b1) + recursive_matrix_mult(a1, b3)
    c2 = recursive_matrix_mult(a2, b0) + recursive_matrix_mult(a3, b2)
    c3 = recursive_matrix_mult(a2, b1) + recursive_matrix_mult(a3, b3)

    top = np.hstack((c0, c1))
    bottom = np.hstack((c2, c3))

    return np.vstack((top, bottom))

def basic_smoke_test():
    """
    Calls strassens and throws `AssertionException` if calculations are not performed as expected.
    """
    smoke1 = [[1, 2], [3, 4]]
    smoke2 = [[5, 6], [7, 8]]
    result = strassens(smoke1, smoke2)
    expected = np.array([[19, 22], [43, 50]])
    assert(np.array_equal(result, expected))
    print("First test passed")

    smoke3 = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13]]
    result = recursive_matrix_mult(smoke3, smoke3)
    expected = np.array([[70, 80, 90, 100], [136, 158, 180, 202], [202, 236, 270, 304], [268, 314, 360, 406]])
    assert(np.array_equal(result, expected))
    print("Second test passed")

## THE STUDENT SHOULD IMPLEMENT STRASSENS MATRIX MULTIPLICATION ALGORITHM
'''
The `strassens` function implements Strassen's algorithm for matrix multiplication, which is an efficient method for multiplying two 
matrices. The function takes two matrices, `A` and `B`, as input parameters and returns their product. Both matrices are converted to 
NumPy arrays to facilitate matrix operations.

The function begins by checking if the matrices are of size 1x1, which is the base case. If they are, it simply returns the product of 
the two single elements. For larger matrices, the function proceeds by dividing each matrix into four quadrants. This is done by 
calculating the midpoint `n` and slicing the matrices accordingly into `A11`, `A12`, `A21`, `A22` for matrix `A` and `B11`, `B12`, 
`B21`, `B22` for matrix `B`.

Next, the function recursively computes seven products (`M1` to `M7`) using combinations of these quadrants. These products are 
essential components of Strassen's algorithm and are calculated using specific combinations of matrix additions and subtractions.

After computing the seven products, the function calculates the four quadrants of the resulting matrix `C` (`C11`, `C12`, `C21`, `C22`) 
using these products. These quadrants are then combined into a single matrix by horizontally and vertically stacking them using NumPy's
`hstack` and `vstack` functions.

Finally, the function returns the combined matrix, which is the product of the input matrices `A` and `B`. This implementation of 
Strassen's algorithm reduces the time complexity of matrix multiplication from O(n^3) to approximately O(n^2.81), making it more 
efficient for large matrices.
'''
def strassens(A, B):
    """
    Uses Strassen’s method for matrix multiplication to return the product of the two
    provided Matrices A and B.
    :param A: the first matrix to multiply. Implemented as a np.array
    :param B: The second matrix to multiply. Implemented as a np.array
    :return: The product of A and B
    """
    A = np.array(A)
    B = np.array(B)
    
    # Base case when the matrix is 1x1
    if A.shape[0] == 1:
        return A * B
    
    # Splitting the matrices into quadrants
    n = A.shape[0] // 2
    A11 = A[:n, :n]
    A12 = A[:n, n:]
    A21 = A[n:, :n]
    A22 = A[n:, n:]
    
    B11 = B[:n, :n]
    B12 = B[:n, n:]
    B21 = B[n:, :n]
    B22 = B[n:, n:]
    
    # Computing the 7 products, recursively (p1, p2...p7)
    M1 = strassens(A11 + A22, B11 + B22)
    M2 = strassens(A21 + A22, B11)
    M3 = strassens(A11, B12 - B22)
    M4 = strassens(A22, B21 - B11)
    M5 = strassens(A11 + A12, B22)
    M6 = strassens(A21 - A11, B11 + B12)
    M7 = strassens(A12 - A22, B21 + B22)
    
    # Computing the values of the 4 quadrants of the final matrix C
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    
    return np.vstack((top, bottom))

if __name__ == "__main__":
    # NOTE THIS IS JUST A BASIC SMOKE TEST.  TO RUN THE FULL TEST SUITE THAT WILL BE USED FOR GRADING USE THE INCLUDED
    # StrassensTester.py.  RUN StrassensTester.py WITH THE PROPER IMPORT STATEMENT IN LINE 2 TO SEE THE RESULTS.
    basic_smoke_test()