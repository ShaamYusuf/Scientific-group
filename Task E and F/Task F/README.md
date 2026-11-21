# TASK F: GAUSSIAN ELIMINATION AND LU DECOMPOSITION

## 1. Introduction

Gaussian elimination and LU decomposition are numerical methods used to solve systems of linear equations. They are important in scientific computing because they provide systematic ways of solving mathematical problems involving multiple unknown variables.

## 2. Mathematical Concept

Gaussian elimination transforms a system of equations into an upper triangular form by eliminating unknown variables. Back-substitution is then used to determine the unknown values.

LU decomposition expresses a coefficient matrix as the product of a lower triangular matrix and an upper triangular matrix. The factorisation can be reused when solving systems with the same coefficient matrix but different measurement vectors.

## 3. Real-World Application

The application involves a scientific simulation that repeatedly receives new measurement values while using the same coefficient matrix.

## 4. Implementation

Python, NumPy and SciPy were used. The coefficient matrix was created using NumPy, while SciPy's `lu_factor()` and `lu_solve()` functions were used to factor the matrix and solve the different measurement systems.

## 5. Results

The program successfully solved three measurement systems.

For the first measurement set, the solution was:

- x = 5
- y = 5
- z = 5

The other measurement sets also produced numerical solutions. Their residual norms were approximately zero, confirming that the calculated solutions satisfied the corresponding systems.

## 6. Parameter Modification

The second measurement vector was changed from [16, 11, 9] to [18, 11, 9]. The new solution was approximately [5.7561, 5.0244, 4.6748].

The result demonstrated that changing the measurement values changes the solution while the original LU factorisation remains reusable.

## 7. Assumptions

- The coefficient matrix remains constant.
- Measurement vectors contain valid numerical values.
- The coefficient matrix is nonsingular.
- Numerical precision is sufficient for the application.

## 8. Conclusion

The task demonstrated how Gaussian elimination and LU decomposition can be used to solve systems of linear equations. LU decomposition is particularly useful when the same coefficient matrix is used with several different measurement vectors because the factorisation only needs to be performed once.
