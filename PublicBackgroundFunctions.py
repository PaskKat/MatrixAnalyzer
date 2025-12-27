
def get_key(dictionary, value_input):
  list_values = []
  list_keys = [key for key in dictionary.keys()]
  list_values = [value for value in dictionary.values()]
  n = 0
  for element in list_values:
    if element == value_input:
      break
    else:
      n += 1
  key_val = list_keys[n]
  return key_val

def get_separate_copy(matrix):
  matrix_copy = [row.copy() for row in matrix]
  return matrix_copy

def get_mn(matrix):
    m = len(matrix)
    n = len(matrix[0])
    return (m, n)

def get_pivot(row):
  pivot_index = 0
  counter = 0
  if 0 not in row:
    pivot_index = 0
    counter += 1
  else:
      if sum(row) == 0 and max(row) == 0:
        pivot_index = -1
        counter += 1
      else:
        for element in row:
          if element != 0:
            pivot_index = row.index(element)
            counter += 1
            break
  return pivot_index

def get_column(matrix,index):
  matrix_copy = get_separate_copy(matrix)
  column = [row[index] for row in matrix_copy]
  return column

def is_zero_vector(vector):
  vector_copy = get_separate_copy(vector)
  for row in vector_copy:
    for element in row:
      if element == 0:
        pass
      else:
        return False
  return True

def is_zero_row(row):
  row_copy = row.copy()
  if max(row_copy) == 0 and sum(row_copy) == 0:
    return True
  return False

def is_close_to(matrix_a,matrix_b):
  matrix_a_copy = get_separate_copy(matrix_a)
  matrix_b_copy = get_separate_copy(matrix_b)
  for row_i in range(0,len(matrix_a_copy)):
    for column_i in range(0,len(matrix_a_copy[0])):
      if abs(matrix_a_copy[row_i][column_i] - matrix_b_copy[row_i][column_i]) >= 1e-16:
        return False
      else:
        pass
  return True

def count_swaps(list_1,list_2):
  list_1_copy = list_1.copy()
  list_2_copy = list_2.copy()
  swapped_list = list_1_copy.copy()
  total_swaps = 0
  for row_index in list_1_copy:
    if row_index not in list_2_copy:
      pass
    else:
      num_swaps = 0
      num_swaps = abs(list_2_copy.index(row_index)-swapped_list.index(row_index))
      total_swaps += num_swaps
      swapped_list.remove(row_index)
      swapped_list.insert(list_2_copy.index(row_index),row_index)
  return total_swaps

def row_add(matrix, index_a, index_b, factor = 1):
  matrix_copy = get_separate_copy(matrix)
  row_a = matrix_copy[index_a]
  row_b = matrix_copy[index_b]
  counter = 0
  for element in row_a:
    sum_rows = element + (factor * row_b[counter])
    row_a[counter] = sum_rows
    counter += 1
  return matrix_copy

def row_swap(matrix, row_a, row_b):
    matrix_copy = get_separate_copy(matrix)
    index_a = matrix_copy.index(row_a)
    index_b = matrix_copy.index(row_b)
    matrix_copy[index_a], matrix_copy[index_b] = matrix_copy[index_b], matrix_copy[index_a]
    return matrix_copy

def factor_row(row):
  row_copy = row.copy()
  if is_zero_row(row_copy) == True:
    factor = 0
    return (row, factor)
  elif is_zero_row(row_copy) == False:
    pivot_index = get_pivot(row_copy)
    factor = row[pivot_index]
    row = []
    for element in row_copy:
      new_num = element / factor
      if (abs(round(new_num) - new_num) <= (1e-15)):
        new_num = round(new_num)
      row.append(new_num)
    return (row,factor)

def simplify_matrix(matrix):
  matrix_copy = get_separate_copy(matrix)
  simplified_matrix = [factor_row(row)[0] for row in matrix_copy]
  return simplified_matrix

def simplify_and_apply(matrix_a,matrix_b):
  matrix_a_copy = get_separate_copy(matrix_a)
  new_matrix_a = []
  matrix_b_copy = get_separate_copy(matrix_b)
  new_matrix_b = []
  new_b_row = []
  for row_index in range(0,len(matrix_a_copy)):
    row_copy = matrix_a_copy[row_index].copy()
    (new_row, row_factor) = factor_row(row_copy)
    new_matrix_a.append(new_row)
    if row_factor != 0:
      row_factor = 1 / row_factor
    new_b_row = [(element * row_factor) for element in matrix_b_copy[row_index]]
    new_matrix_b.append(new_b_row)
  return (new_matrix_a, new_matrix_b)

def factor_matrix(matrix):
  matrix_copy = get_separate_copy(matrix)
  simplified_matrix = []
  factors_product = 1
  for row in matrix_copy:
    (row, factor) = factor_row(row)
    factors_product *= factor
    simplified_matrix.append(row)
  return (simplified_matrix,factors_product)

def sort_rows(matrix):
  matrix_copy = get_separate_copy(matrix)
  row_dict = {}
  counter = 0
  for row in matrix_copy:
    pivot_index = get_pivot(row)
    row_dict[counter] = pivot_index
    counter += 1
  old_indexes = [key for key in row_dict.keys()]
  sorted_values = [value for value in sorted(row_dict.values())]
  sorted_indexes = []
  for value in sorted_values:
    if value != -1:
      sorted_indexes.append(get_key(row_dict,value))
      del row_dict[get_key(row_dict,value)]
  for value in sorted_values:
      if value == -1:
        sorted_indexes.append(-1)
  sorted_matrix = []
  num_swaps = count_swaps(old_indexes,sorted_indexes)
  for index in sorted_indexes:
    if index != -1:
      sorted_matrix.append(matrix_copy[index])
  n = len(matrix_copy[index])
  for index in sorted_indexes:
    if index == -1:
      zero_row = [0 for num in range(0,n)]
      sorted_matrix.append(zero_row)
  return (sorted_matrix, num_swaps)

def sort_and_apply(matrix_a,matrix_b):
  matrix_a_copy = get_separate_copy(matrix_a)
  matrix_b_copy = get_separate_copy(matrix_b)
  row_dict = {}
  counter = 0
  for row in matrix_a_copy:
    pivot_index = get_pivot(row)
    row_dict[counter] = pivot_index
    counter += 1
  sorted_values = [value for value in sorted(row_dict.values())]
  sorted_indexes = []
  for value in sorted_values:
    if value != -1:
      sorted_indexes.append(get_key(row_dict,value))
      del row_dict[get_key(row_dict,value)]
    elif value == -1:
      sorted_indexes.append(-1)
  sorted_matrix_a = []
  sorted_matrix_b = []
  for index in sorted_indexes:
    if index != -1:
      sorted_matrix_a.append(matrix_a_copy[index])
      sorted_matrix_b.append(matrix_b_copy[index])
  return (sorted_matrix_a,sorted_matrix_b)