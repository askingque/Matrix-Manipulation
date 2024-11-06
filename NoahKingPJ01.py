def reverse_list(lst):
#reverse_list reverses the order of elements in a list
#:param lst: A list to be reversed
#:return: A reversed copy of lst
#:time complexity: O(n), where n is the number of elements in lst
    listLen = len(lst) - 1
    returnList = []
    for i, n in enumerate(lst):
        returnList.append(lst[listLen-i])
    return returnList

def copy_matrix(matrix):
#copy_matrix copies a 2D list
#:param matrix: A 2D list to be copied
#:return: A copy of matrix
#:time complexity: O(n), where n is the number of elements in matrix
    returnMatrix = []
    for row in matrix:
        returnMatrix.append(row[:])
    return returnMatrix

def pretty_print(matrix):

#pretty_print prints out 2D lists in an easier to read format than built-in
#print.
#:param matrix: A 2D list
#:return: None
#:time complexity: O(n), where n is the number of elements in matrix
    for row in matrix:
        print(row)
        print()

def transpose_major(matrix, in_place = False):
#transpose_major transposes a 2D lists accross the major diagonal. Can transpose either in-place or not depending on user-preference or project requirements
#:param matrix: A SQUARE 2D list to be transposed
#:param in_place: determines whether matrix is transposed in-place or as a copy
#:return t_matrix: Either a reference to a 2D list (if transposed in-place) or a
#transposed copy of a 2D list
#:time complexity: O(n), where n is the number of elements in matrix
    if in_place:
        t_matrix = matrix
        for i in range(len(matrix)):
            for j in range(i):
                t_matrix[i][j], t_matrix[j][i] = t_matrix[j][i], t_matrix[i][j]
        return t_matrix
    else:
        t_matrix = copy_matrix(matrix)
        return [[t_matrix[j][i] for j in range(len(t_matrix))] for i in range(len(t_matrix[0]))]
    
def transpose_minor(matrix, in_place = False):
#transpose_minor transposes a 2D lists accross the minor diagonal. Can transpose either in-place or not depending on user-preference or project requirements
#:param matrix: A SQUARE 2D list to be transposed
#:param in_place: determines whether matrix is transposed in-place or as a copy
#:return t_matrix: Either a reference to a 2D list (if transposed in-place) or a
#transposed copy of a 2D list
#:time complexity: O(n), where n is the number of elements in matrix
    matrix_width = len(matrix[0]) - 1
    if in_place:
        t_matrix = matrix
        for i in range(len(matrix)):
            for j in range(i):
                t_matrix[matrix_width-i][j], t_matrix[matrix_width-j][i] = t_matrix[matrix_width-j][i], t_matrix[matrix_width-i][j]
    else:
        t_matrix = copy_matrix(matrix)
        for i in range(len(matrix)):
            for j in range(i):
                t_matrix[matrix_width-i][j], t_matrix[matrix_width-j][i] = t_matrix[matrix_width-j][i], t_matrix[matrix_width-i][j]
    return t_matrix

def reverse_matrix_rows(matrix, in_place = False):
#reverse_matrix_rows reverses the order of the rows in a 2D list. Can reverse either in-place or not depending on user-preference or project requirements
#:param matrix: A 2D list to have its rows reversed
#:param in_place: determines whether matrix is reversed in-place or as a copy
#:return rev_matrix: Either a reference to a 2D list (if reversed in-place) or a reversed copy of a 2D list
#:time complexity: O(sqrt(n)), where n is the number of elements in matrix
    if in_place:
        rev_matrix = matrix
        matrixLen = len(matrix) - 1
        for i in range(matrixLen//2 + 1):
            rev_matrix[i], rev_matrix[matrixLen-i] = rev_matrix[matrixLen-i], rev_matrix[i]

    else:
        rev_matrix = copy_matrix(matrix)
        matrixLen = len(matrix) - 1
        for i in range(matrixLen//2 + 1):
            rev_matrix[i], rev_matrix[matrixLen-i] = rev_matrix[matrixLen-i], rev_matrix[i]

    return rev_matrix

def rotate(matrix):
#rotate rotates a 2D list 90 degrees counter-clockwise
#:param matrix: A 2D list to be rotated
#:return rotated_matrix: A 2D list that is a 90 degree counter-clockwise rotation of matrix
#:time complexity: O(n), where n is the number of elements in matrix
# calculate size
    size = len(matrix)
    if size >= 4: # I should be able to change this 4 to any value > 0
# rotate counter-clockwise in place
        rotated_matrix = matrix
        transpose_major(rotated_matrix, in_place = True)
        reverse_matrix_rows(rotated_matrix, in_place = True)
# HINT: Using a reference assignment to modify something counts as in-place!
    else:
        rotated_matrix = copy_matrix(matrix)
        rotated_matrix = transpose_minor(rotated_matrix)
        rotated_matrix = reverse_matrix_rows(rotated_matrix)
# rotate clockwise as copy (not in-place)
    return rotated_matrix

def check_match(big_matrix, small_matrix, start_row, start_col):
#check_match checks if a small matrix is present in a larger matrix at a given starting row and column
#:param big_matrix: A 2D list that may contain small_matrix
#:param small_matrix: A 2D list that may be contained in big_matrix
#:param start_row: The row in big_matrix where the top left corner of small_matrix is being checked
#:param start_col: The column in big_matrix where the top left corner of small_matrix is being checked
#:return: True if small_matrix is found in big_matrix, False otherwise
#:time complexity: O(n), where n is the number of elements in small_matrix
    for i in range(len(small_matrix)):
        for j in range(len(small_matrix[0])):
            if big_matrix[start_row + i][start_col + j] != small_matrix[i][j]:
                return False
    return True
# returns True or False, depending on whether a match was found

def count_appearances(big_matrix, small_matrix):
#count_appearances counts the number of times a small matrix appears in a big matrix at any rotation
#:param big_matrix: A 2D list that may contain small_matrix
#:param small_matrix: A 2D list that may be contained in big_matrix
#:return: A list of length 4, where each element is the number of times small_matrix appears in big_matrix at 0, 90, 180, and 270 degree rotations
#:time complexity: O(n^2), number of elements in big_matrix times the number of elements in small_matrix
# YOUR CODE BELOW
    counts = [0,0,0,0] # counts for 0, 90, 180, 270 degree rotations
    for i in range(len(big_matrix) - len(small_matrix) + 1):
        for j in range(len(big_matrix[0]) - len(small_matrix[0]) + 1):
            for k in range(4):
                if check_match(big_matrix, small_matrix, i, j):
                    counts[k] += 1
                small_matrix = rotate(small_matrix)
# YOUR CODE ENDS
    return counts

def main(file_path):
    with open(file_path, 'r') as file:
        while True:
# read in big_size, small_size as ints
            big_size, small_size = map(int, file.readline().strip().split())
            if big_size == 0 and small_size == 0:
                break
                print([0,0,0,0])
# read in big_matrix as 2D list of chars
            big_matrix = [list(file.readline().strip()) for _ in range(big_size)]
# read in small_matrix as 2D list of chars
            small_matrix = [list(file.readline().strip()) for _ in range(small_size)]
            
            counts = count_appearances(big_matrix, small_matrix)
            print(counts)
# DRIVER CODE (DO NOT MODIFY)
file_path = 'input.txt'
main(file_path)

# EXAMPLE TEST CODE
def initialize_test_matrix():
    return [
['A', 'B', 'C'],
['D', 'E', 'F'],
['G', 'H', 'I']
]

def test_reverse_matrix_rows():
    original_matrix = initialize_test_matrix()
    test_matrix = initialize_test_matrix()
    rev_matrix = reverse_matrix_rows(test_matrix, in_place=False)
    assert rev_matrix == list(reversed(test_matrix)), "reverse_matrix_rows not working as intended when in_place == False"
    rev_matrix = reverse_matrix_rows(original_matrix, in_place=True)
    assert rev_matrix == original_matrix, "reverse_matrix_rows not working as intended when in_place == True"

def test_transpose(function, matrix, in_place):
    print(f"\n####### Testing {function.__name__}: in_place = {in_place} #######\n")
    if in_place == False:
        t_matrix =  (function(matrix, in_place))
        t_matrix[0][1] = 23
        pretty_print(t_matrix)
        assert t_matrix != matrix, "not working if in_place == False"
    if in_place == True:
        t_matrix = function(matrix, in_place)
        t_matrix[0][1] = 23
        pretty_print(t_matrix)
        assert t_matrix == matrix, "not working if in_place == True"

test_reverse_matrix_rows()

test_matrix = initialize_test_matrix()
test_transpose(transpose_major, test_matrix, in_place=False)
test_matrix = initialize_test_matrix()
test_transpose(transpose_minor, test_matrix, in_place=False)
test_matrix = initialize_test_matrix()
test_transpose(transpose_major, test_matrix, in_place=True)
test_matrix = initialize_test_matrix()
test_transpose(transpose_minor, test_matrix, in_place=True)
