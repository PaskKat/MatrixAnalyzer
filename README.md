# MatrixAnalyzer
### Author: PaskKat
### Developed: October 26, 2024 - March 21, 2025

## Purpose: 
Independently recreate common linear algebra tools in python to understand how scipy.linalg works. This repo uses no imported libraries (as a challenge) to understand how scipy operates. Only python's most basic functions are used.

## Running Matrix Analyzer (Command Line):
1. Paste into the command line: 'git clone https://github.com/PaskKat/MatrixAnalyzer' 
2. Enter into the MatrixAnalyzer folder by entering in the command line: 'cd MatrixAnalyzer/'
3. Run the analysis in the command line with: 'python3 PublicMatrixAnalyzer.py'
4. Enter the dimensions of the prospective matrix as (Number of Rows)x(Number of Columns)
   - (Ex. 3x2)
5. Enter the elements of each row as (element) (element) (element) with a space to differentiate elements and return to start another row. Repeat as needed.
   - (Ex. -1 2.00 3.5) for a 3-term row.

## Functions: PublicBackgroundFunctions.py 

Note: All matricies are stored as 2D arrays (python lists).

1. Data Parsing
   - Get a dictionary's key given its value
   - Get independent copy of any mxn matrix
   - Get the dimensions (m and n) of any mxn matrix
   - Get the index of the first nonzero number in the row (list)
   - Get all elements in a given matrix column
   - (True or False) Whether or not a matrix column contains all zeros
   - (True or False) Whether or not a row (list) contains all zeros
   - (True of False) if every matrix a element within 1e-16 (max digits) of matrix b's elements
   - Get the number of list interchanges to go from list 1 to list 2
2. Row Operations
   - Add factor * row_b to row_a
   - Switch the place of the two rows row_a and row_b in a matrix
   - Get a given row reduced to one at the first nonzero term, and what it divided the row by
3. Matrix Operations
   - Simplify all rows in a matrix by their first nonzero terms
   - Simplify matrix a and apply all row operations done on a to matrix b
   - Simplify all rows in the matrix and get the product of their factors
   - Sort rows in order of least amount of leading zeros, get the number of row operations taken
   - Sorts matrix a (as above) and apply all operations to matrix b

## Functions: PublicLinearAlgebraOperations.py

1. Input arbitrary mxn matricies (' ' indicates column, '\n' indicates row)
   - Find the m,n of any [[],...,[]] matrix
2. Matrix and Vector Arithmetic
   - Scalar multiplication mxn matrix
   - Add/subtract mxn matricies
   - Multiply mxn matricies
   - Scaling down matricies
   - Dimension of any vector
   - Magnitude of any vector
   - Dot product
   - Cross product
   - Normalization
3. Transpose arbitrary matricies
4. Identity matrix generate for any nxn dimensions
5. "Solving". Gaussian Elimination
    - All row-equivalent operations
    - Row-Echelon Form (REF)
    - Reduced Row Echelon Form (RREF)
6. Trace of any nxn matrix
7. Determinant of any nxn matrix
8. Inverse Matrix Calculator
9. Eigenvalues (Power method & deflation)
   - Dominant Eigenvalue
10. Eigenvectors (Power method & deflation)
    - Dominant Eigenvector

## Functions: PublicMatrixAnalyzer.py 

Note: Matrix Analysis (user input, etc) is called automatically when this file runs.
1. User Input arbitrary mxn matricies (' ' indicates column, '\n' indicates row)
2. Analyze inputted mxn matrix for: 
   - Dimensions, Transpose, REF, RREF, Trace, Determinant, Real Eigenvalues, Real Eigenvectors
