# TASK E: SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

## 1. Introduction

Systems of linear equations are used in scientific computing to determine unknown quantities from known relationships. This task demonstrates how Python and NumPy can solve simultaneous equations using matrix operations.

## 2. Mathematical Concept

A system of linear equations can be represented as Ax = b, where A is the coefficient matrix, x contains the unknown variables and b contains the known constants.

The solution is the set of values that satisfies all the equations.

## 3. Real-World Application

The application involves a technology company operating two types of servers. Type A uses 4 CPU units and 8 GB of memory, while Type B uses 2 CPU units and 12 GB of memory. The total resource usage is 20 CPU units and 72 GB of memory.

## 4. Implementation

Python and NumPy were used to create the coefficient matrix and the constant vector. The function `np.linalg.solve()` was used to calculate the unknown server quantities.

## 5. Results

The program produced the following results:

- Type A servers: 3
- Type B servers: 4

The verification produced [20, 72], confirming that the calculated values satisfy the original equations.

## 6. Parameter Modification

The CPU requirement was changed from 20 to 24 units while the memory requirement remained at 72 GB. The new solution was 4 Type A servers and 3 Type B servers.

This demonstrates that changing the known resource requirements affects the solution.

## 7. Assumptions

- Each server type has fixed resource requirements.
- The measurements are accurate.
- The relationship between server quantities and resource usage is linear.
- Server quantities must be whole numbers.

## 8. Conclusion

The task demonstrated how systems of linear equations can be solved using NumPy. Matrix representation and the `np.linalg.solve()` function provide an efficient method of determining unknown quantities in scientific and engineering problems.
