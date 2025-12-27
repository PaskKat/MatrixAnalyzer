from PublicBackgroundFunctions import *

def get_matrix():
    print("\n------------------------------------------------------------------------\n")
    inputted_matrix = []
    mxn_input = str(input("mxn: "))
    m = int(mxn_input.split("x")[0])
    n = int(mxn_input.split("x")[1])
    if m == 0 or n == 0:
      return [[]]
    elif m!= 0 and n != 0:
      for number in range(0,m):
        strings = (input("").split(" "))
        numbers = []
        if '' in strings:
          strings.remove('')
        else:
          pass
        for string in strings:
            number = float(string)
            numbers.append(number)
        inputted_matrix.append(numbers)
        numbers = []
      return inputted_matrix

def get_vector():
    print("\n------------------------------------------------------------------------\n")
    string = (input("Vector: "))
    input_vector = string.split(" ")
    if '' in input_vector:
       input_vector.remove('')
    user_vector = [float(eval(x)) for x in input_vector]
    return user_vector

def scale_matrix(matrix,factor):
  matrix_copy = get_separate_copy(matrix)
  scaled_matrix = []
  for row in matrix_copy:
    new_row = []
    for element in row:
      new_element = element * factor
      if abs(round(new_element)-new_element) <= 1e-15:
        new_element = round(new_element)
      new_row.append(new_element)
    scaled_matrix.append(new_row)
  return scaled_matrix

def add_matricies(matrix_a,matrix_b,scale_a = 1,scale_b = 1):
  matrix_a_copy = scale_matrix(get_separate_copy(matrix_a),scale_a)
  matrix_b_copy = scale_matrix(get_separate_copy(matrix_b),scale_b)
  new_matrix = []
  (a_m, a_n) = get_mn(matrix_a_copy)
  (b_m, b_n) = get_mn(matrix_b_copy)
  if (a_m != b_m) or (a_n != b_n):
    new_matrix = "DNE"
  else:
    for row_index in range(0,a_m):
      new_row = []
      for element_index in range(0,a_n):
        new_el = matrix_a_copy[row_index][element_index] + matrix_b_copy[row_index][element_index]
        if abs(round(new_el)-new_el) <= 1e-15:
          new_el = round(new_el)
        new_row.append(new_el)
      new_matrix.append(new_row)
  return new_matrix

def multiply_matricies(matrix_a,matrix_b):
  matrix_a_copy = get_separate_copy(matrix_a)
  matrix_b_copy = get_separate_copy(matrix_b)
  a_n = get_mn(matrix_a)[1]
  b_m = get_mn(matrix_b)[0]
  if a_n != b_m:
    new_matrix = "DNE"
  else:
    new_matrix = []
    for row_index in range(0,len(matrix_a_copy)):
      new_row = []
      for column_index in range(0,len(matrix_b_copy[0])):
        column_list = get_column(matrix_b_copy,column_index)
        new_el = 0
        for element_index in range(0,len(matrix_a_copy[row_index])):
          a_el = matrix_a_copy[row_index][element_index]
          b_el = column_list[element_index]
          new_el += a_el * b_el
        new_row.append(new_el)
      new_matrix.append(new_row)
  return new_matrix

def scale_down(matrix):
  matrix_copy = get_separate_copy(matrix)
  greatest_val = 0
  for row in matrix_copy:
    for element in row:
      if abs(element) > abs(greatest_val):
        greatest_val = element
  if greatest_val == 0:
    factored_matrix = scale_matrix(matrix_copy,0)
  else:
    factor = 1/greatest_val
    factored_matrix = scale_matrix(matrix_copy, factor)
  return factored_matrix

def dim(vector):
  dimension = len(vector)
  return dimension

def magnitude(vector):
  vector_copy = vector.copy()
  value_holder = []
  for component in vector_copy:
    squared_component = component ** 2
    value_holder.append(squared_component)
  sum_values = 0
  for value in value_holder:
    sum_values += value
  magnitude = sum_values ** (0.5)
  return magnitude

def dot(vector_a, vector_b):
  vector_a_copy = vector_a.copy()
  vector_b_copy = vector_b.copy()
  if len(vector_a_copy) != len(vector_b_copy):
    dot_product = "DNE"
  else:
    dot_product = 0
    for element_index in range(0,len(vector_a)):
      dot_product += vector_a[element_index] * vector_b[element_index]
  return dot_product

def cross(vector_a, vector_b):
  vector_a_copy = vector_a.copy()
  vector_b_copy = vector_b.copy()
  el_1 = (vector_a_copy[1]*vector_b_copy[2])-(vector_a_copy[2]*vector_b_copy[1])
  el_2 = (vector_a_copy[2]*vector_b_copy[0])-(vector_a_copy[0]*vector_b_copy[2])
  el_3 = (vector_a_copy[0]*vector_b_copy[1])-(vector_a_copy[1]*vector_b_copy[0])
  cross_product = [el_1, el_2, el_3]
  return cross_product

def normalize_column(vector):
  vector_copy = get_separate_copy(vector)
  normalized_vector = []
  square_magnitude = 0
  for row in vector_copy:
    square_magnitude += row[0] ** 2
  magnitude = square_magnitude ** 0.5
  if magnitude == 0:
    normalized_vector = scale_matrix(vector_copy,0)
  else:
    for row in vector_copy:
      new_row = []
      new_component = row[0]/magnitude
      new_row.append(new_component)
      normalized_vector.append(new_row)
  return normalized_vector

def normalize_row(vector):
  vector_copy = vector.copy()
  square_magnitude = sum([x**2 for x in vector_copy])
  magnitude = square_magnitude ** 0.5
  if magnitude == 0:
    normalized_vector = [0 for x in vector_copy]
  else:
    normalized_vector = [x/magnitude for x in vector_copy]
  return normalized_vector

def identity_matrix(max_n):
  m = 0
  identity_matrix = []
  while m < max_n:
    row_list = []
    if m == 0:
      row_list.append(1)
      for num in range(1,max_n):
        row_list.append(0)
    elif m != 0:
      for num in range(0,m):
        row_list.append(0)
      row_list.append(1)
      for num in range(m, max_n - 1):
        row_list.append(0)
    identity_matrix.append(row_list)
    m += 1
  return identity_matrix

def transpose(matrix):
  matrix_copy = get_separate_copy(matrix)
  list_column = []
  transpose_matrix = []
  index_counter = 0
  while index_counter < len(matrix[0]):
    list_column = [row[index_counter] for row in matrix_copy]
    transpose_matrix.append(list_column)
    list_column = []
    index_counter += 1
  return transpose_matrix
  
def ref(matrix):
  matrix_copy = get_separate_copy(matrix)
  counter = 0
  column_index = 0
  matrix_copy = sort_rows(simplify_matrix(matrix_copy))[0]
  for row_counter in range(counter, len(matrix_copy)):
    row = matrix_copy[row_counter]
    matrix_copy = simplify_matrix(matrix_copy)
    column_index = get_pivot(row)
    if column_index == -1:
      pass
    elif column_index != -1:
      for index in range(counter+1, len(matrix_copy)):
        sub_row = matrix_copy[index]
        if sub_row[column_index] != 0:
          matrix_copy = row_add(matrix_copy,index,counter,-1)
    counter += 1
  matrix_copy = sort_rows(matrix_copy)[0]
  return matrix_copy

def rref(matrix):
  matrix_copy = get_separate_copy(matrix)
  matrix_copy = ref(matrix_copy)
  for row_index in range(0,len(matrix_copy)):
    index_a = row_index
    pivot_index_a = get_pivot(matrix_copy[index_a])
    for sub_row_index in range((index_a + 1),len(matrix_copy)):
      index_b = sub_row_index
      pivot_index_b = get_pivot(matrix_copy[index_b])
      if pivot_index_a < pivot_index_b and pivot_index_a != -1:
        val_a = matrix_copy[index_a][pivot_index_b]
        val_b = matrix_copy[index_b][pivot_index_b]
        factor = val_a/val_b
        matrix_copy = row_add(matrix_copy,index_a,index_b, -1 * factor)
  matrix_copy = simplify_matrix(matrix_copy)
  return matrix_copy

def trace(matrix):
  matrix_copy = get_separate_copy(matrix)
  (m,n) = get_mn(matrix_copy)
  if m != n:
    trace = "DNE"
  else:
    trace = 0
    for index in range(0,n):
      trace += matrix_copy[index][index]
  return trace

def det(matrix):
  matrix_copy = get_separate_copy(matrix)
  (m,n) = get_mn(matrix_copy)
  if m!=n:
    return "DNE"
  determinant = 1
  total_swaps = 0
  (matrix_copy,factor) = factor_matrix(matrix_copy)
  determinant *= factor
  (matrix_copy,num_swaps) = sort_rows(matrix_copy)
  total_swaps += num_swaps
  counter = 0
  column_index = 0
  for row_counter in range(counter, len(matrix_copy)):
    row = matrix_copy[row_counter]
    (matrix_copy,product) = factor_matrix(matrix_copy)
    determinant *= product
    column_index = get_pivot(row)
    if column_index == -1:
      pass
    elif column_index != -1:
      for index in range(counter+1, len(matrix_copy)):
        sub_row = matrix_copy[index]
        if sub_row[column_index] != 0:
          matrix_copy = row_add(matrix_copy,index,counter,-1)
    counter += 1
  (matrix_copy,num_swaps) = sort_rows(matrix_copy)
  total_swaps += num_swaps
  if total_swaps % 2 != 0:
    determinant = determinant * -1
  return determinant

def inverse(matrix):
  matrix_copy = get_separate_copy(matrix)
  m = get_mn(matrix_copy)[0]
  n = get_mn(matrix_copy)[1]
  zero_row = []
  for number in range(0,n):
    zero_row.append(0)
  i_matrix = identity_matrix(m)
  if rref(matrix_copy) != i_matrix:
    inverse_matrix = "DNE"
  elif zero_row in matrix_copy:
    inverse_matrix = "DNE"
  else:
    counter = 0
    column_index = 0
    (matrix_copy,i_matrix) = simplify_and_apply(matrix_copy,i_matrix)
    (matrix_copy,i_matrix) = sort_and_apply(matrix_copy, i_matrix)
    for row_counter in range(counter, len(matrix_copy)):
      row = matrix_copy[row_counter]
      (matrix_copy,i_matrix) = simplify_and_apply(matrix_copy,i_matrix)
      column_index = get_pivot(row)
      for index in range(counter+1, len(matrix_copy)):
        sub_row = matrix_copy[index]
        if sub_row[column_index] != 0:
          matrix_copy = row_add(matrix_copy,index,counter,-1)
          i_matrix = row_add(i_matrix,index,counter,-1)
      counter += 1
    (matrix_copy,i_matrix) = simplify_and_apply(matrix_copy,i_matrix)
    for row_index in range(0,len(matrix_copy)):
      index_a = row_index
      pivot_index_a = get_pivot(matrix_copy[index_a])
      for sub_row_index in range((index_a + 1),len(matrix_copy)):
        index_b = sub_row_index
        pivot_index_b = get_pivot(matrix_copy[index_b])
        if pivot_index_a < pivot_index_b and pivot_index_a != -1:
          val_a = matrix_copy[index_a][pivot_index_b]
          val_b = matrix_copy[index_b][pivot_index_b]
          factor =(val_a/val_b)
          matrix_copy = row_add(matrix_copy,index_a,index_b, -1 * factor)
          i_matrix = row_add(i_matrix,index_a,index_b, -1 * factor)
    (matrix_copy,i_matrix) = simplify_and_apply(matrix_copy,i_matrix)
    inverse_matrix = i_matrix
  return inverse_matrix

def dominant_eigenvector(matrix):
  matrix_copy = get_separate_copy(matrix)
  (m,n) = get_mn(matrix_copy)
  if matrix_copy != transpose(matrix_copy) or (m != n):
    return "DNE"
  test_vector = []
  for number in range(0,n):
    test_vector.append([1])
  mul_1 = multiply_matricies(matrix_copy,test_vector)
  mul_2 = multiply_matricies(matrix_copy, mul_1)
  while is_close_to(scale_down(mul_1),scale_down(mul_2)) == False:
    mul_1 = scale_down(mul_2)
    mul_2 = scale_down(multiply_matricies(matrix_copy, mul_2))
  dominant_vector = scale_down(mul_2)
  return dominant_vector

def dominant_eigenvalue(matrix):
  matrix_copy = get_separate_copy(matrix)
  (m,n) = get_mn(matrix_copy)
  if matrix_copy != transpose(matrix_copy) or (m != n):
    return "DNE"
  dom_eigenvector = dominant_eigenvector(matrix_copy)
  scaled_eigenvector = multiply_matricies(matrix_copy,dom_eigenvector)
  if is_zero_vector(scaled_eigenvector) == True:
    eigenvalue = 0
  else:
    for r in range(0,len(dom_eigenvector)):
      for c in range(0,len(dom_eigenvector[r])):
        if dom_eigenvector[r][c] != 0:
          eigenvalue = scaled_eigenvector[r][c]/dom_eigenvector[r][c]
          break
        break
  return eigenvalue

def eigenvalues(matrix):
  matrix_copy = get_separate_copy(matrix)
  (m,n) = get_mn(matrix_copy)
  if matrix_copy != transpose(matrix_copy):
    return "Contains imaginary eigenvalues"
  elif (m != n):
    return "DNE"
  evectors = []
  evalues = []
  dom_eigenvector = dominant_eigenvector(matrix_copy)
  dom_eigenvalue = dominant_eigenvalue(matrix_copy)
  evectors.append(dom_eigenvector)
  evalues.append(dom_eigenvalue)
  evector = get_separate_copy(dom_eigenvector)
  evalue = dom_eigenvalue
  new_matrix = matrix_copy.copy()
  counter = 1
  while counter <= n:
    evector = normalize_column(evector)
    evector_t = transpose(evector)
    transpose_product = multiply_matricies(evector,evector_t)
    subtractant = scale_matrix(transpose_product,evalue)
    new_matrix = add_matricies(matrix_copy,subtractant,1,-1)
    evector = dominant_eigenvector(new_matrix)
    evalue = dominant_eigenvalue(new_matrix)
    matrix_copy = new_matrix
    if (evector in evectors) or (is_zero_vector(evector) == True):
      pass
    else:
      evectors.append(evector)
      evalues.append(evalue)
    counter += 1
  return evalues

def eigenvectors(matrix):
  matrix_copy = get_separate_copy(matrix)
  (m,n) = get_mn(matrix_copy)
  if (matrix_copy != transpose(matrix_copy)):
    return "Contains imaginary eigenvectors"
  elif (m != n):
    return "DNE"
  evectors = []
  evalues = []
  dom_eigenvector = dominant_eigenvector(matrix_copy)
  dom_eigenvalue = dominant_eigenvalue(matrix_copy)
  evectors.append(dom_eigenvector)
  evalues.append(dom_eigenvalue)
  evector = get_separate_copy(dom_eigenvector)
  evalue = dom_eigenvalue
  new_matrix = matrix_copy.copy()
  counter = 1
  while counter <= n:
    evector = normalize_column(evector)
    evector_t = transpose(evector)
    transpose_product = multiply_matricies(evector,evector_t)
    subtractant = scale_matrix(transpose_product,evalue)
    new_matrix = add_matricies(matrix_copy,subtractant,1,-1)
    evector = dominant_eigenvector(new_matrix)
    evalue = dominant_eigenvalue(new_matrix)
    matrix_copy = new_matrix
    if (evector in evectors) or (is_zero_vector(evector) == True):
      pass
    else:
      evectors.append(evector)
      evalues.append(evalue)
    counter += 1
  return evectors
