import copy


        



def pretty_print(matrix):

#pretty_print prints out 2D lists in an easier to read format than built-in
#print.
#:param matrix: A 2D list
#:return: None
#:time complexity: Runs in O(n^2) time, where n is the number of rows or columns
#in matrix
#because esach element in each row of the matrix is printed
#once

    for row in matrix:
        print(row)
        print()

def transpose_major(matrix, in_place = False):
#transpose_major transposes a 2D lists accross the major diagonal. Can transpose
#either in-place or not
#depending on user-preference or project requirements
#:param matrix: A 2D list to be transposed
#:param in_place: determines whether matrix is transposed in-place or as a copy
#:return t_matrix: Either a reference to a 2D list (if transposed in-place) or a
#transposed copy of a 2D list
#:time complexity: ???????????????????????????? (You fill this in based on your
#code)
    if in_place:
        t_matrix = matrix
        for i in range(len(matrix)):
            for j in range(i):
                t_matrix[i][j], t_matrix[j][i] = t_matrix[j][i], t_matrix[i][j]
        return t_matrix
    else:
        t_matrix = copy.deepcopy(matrix)
        return [[t_matrix[j][i] for j in range(len(t_matrix))] for i in range(len(t_matrix[0]))]
    
def transpose_minor(matrix, in_place = False):
    if in_place:
        t_matrix = matrix
        for i in range(len(matrix)):
            for j in range(i):
                t_matrix[i][j], t_matrix[j][i] = t_matrix[j][i], t_matrix[i][j]
        return t_matrix
    else:
        t_matrix = copy.deepcopy(matrix)
        return [[t_matrix[j][i] for j in range(len(t_matrix))] for i in range(len(t_matrix[0]))]
    return t_matrix

def reverse_matrix_rows(matrix, in_place = False):

    return rev_matrix
def rotate(matrix):
    size = len(matrix)
# calculate size
    if size >= 4: # I should be able to change this 4 to any value > 0
# rotate counter-clockwise in place
        pass
# HINT: Using a reference assignment to modify something counts as in-place!
    else:
# rotate clockwise as copy (not in-place)
        return rotated_matrix
def check_match(big_matrix, small_matrix, start_row, start_col):

# returns True or False, depending on whether a match was found
    return

def count_appearances(big_matrix, small_matrix):
    counts = [0,0,0,0] # counts for 0, 90, 180, 270 degree rotations
# YOUR CODE BELOW
# YOUR CODE ENDS
    return counts

def main(file_path):
    with open(file_path, 'r') as file:
        while True:
# read in big_size, small_size as ints
# read in big_matrix as 2D list of chars
# read in small_matrix as 2D list of chars
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
    assert rev_matrix == list(reversed(test_matrix)), #reverse_matrix_rows notworking as intended when in_place == False
    rev_matrix = reverse_matrix_rows(original_matrix, in_place=True)
    assert rev_matrix == original_matrix, #reverse_matrix_rows not working asintended when in_place == True

def test_transpose(function, matrix, in_place):
    print(f"\n####### Testing {function.__name__}: in_place = {in_place} #######\n")
    if in_place == False:
        t_matrix = function(matrix, in_place)
        t_matrix[0][1] = 23
        pretty_print(t_matrix)
        assert t_matrix != matrix, "not working if in_place == False"
    else:
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