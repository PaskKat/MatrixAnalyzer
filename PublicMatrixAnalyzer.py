
from PublicBackgroundFunctions import *
from PublicLinearAlgebraOperations import *

def analyze_matrix(matrix):
    print(f"\n------------------------------------------------------------------------")
    print(f"Matrix:\n")
    for row in matrix:
        print(row)
    mxn = get_mn(matrix)
    m = mxn[0]
    n = mxn[1]
    print(f"\nmxn: {m} x {n}")
    transposed_matrix = transpose(matrix)
    print(f"\nTransposed Form:\n")
    for row in transposed_matrix:
        print(row)
    ref_matrix = ref(matrix)
    print(f"\nRow-Echelon Form:\n")
    for row in ref_matrix:
        print(row)
    rref_matrix = rref(matrix)
    print(f"\nReduced Row-Echelon Form:\n")
    for row in rref_matrix:
        print(row)
    trace_value = trace(matrix)
    print(f"\nTrace: {trace_value}")
    determinant  = det(matrix)
    print(f"\nDeterminant: {determinant}")
    inverse_matrix = inverse(matrix)
    if inverse_matrix == "DNE":
        print("\nInverse: DNE")
    else:
        print(f"\nInverse:\n")
        for row in inverse_matrix:
            print(row)
    eigenvalue_list = eigenvalues(matrix)
    print("\nEigenvalues: ",end = "")
    if eigenvalue_list == "DNE":
      print("DNE")
    elif eigenvalue_list == "Contains imaginary eigenvalues":
       print("Contains imaginary eigenvalues")
    else:
      for eigenvalue in eigenvalue_list[0:-1]:
        print(eigenvalue,", ",end = "")
      print(eigenvalue_list[-1])
    eigenvector_list = eigenvectors(matrix)
    print("\nEigenvectors: ",end = "")
    if eigenvector_list == "DNE":
      print("DNE")
    elif eigenvector_list == "Contains imaginary eigenvectors":
       print("Contains imaginary eigenvectors")
    else:
      print()
      for eigenvector in eigenvector_list:
        print(eigenvector)
    print(f"\n------------------------------------------------------------------------")

user_matrix = get_matrix()
analyze_matrix(user_matrix)
