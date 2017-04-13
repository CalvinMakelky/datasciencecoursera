def is_diagonal_matrix(matrix):
	one_index = 0 # variable used to store the index of the 1's in each row of the matrix
	if matrix[one_index][one_index] == 1: # if the diagonal begins on the left
		for i in matrix: # iterates through the lists in the matrix
			for index, j in enumerate(i): # iterates through the list, keeps an index of the element
				if index == one_index and j != 1: # if it is at the index where a 1 is expected and the value is not a 1
					return False
				elif index != one_index and j != 0: # if the value is not 0 anywhere else
					return False
			one_index += 1 # increment the index where a 1 is expected
		return True
	elif matrix[one_index][len(matrix[one_index]) - 1] == 1: # if the diagonal begins on the right
		one_index = len(matrix[one_index]) - 1 # begin at the left
		for i in matrix:
			for index, j in enumerate(i):
				if index == one_index and j != 1:
					return False
				elif index != one_index and j != 0:
					return False
			one_index -= 1 # decrement the expected index (diagonal is going toward the left)
		return True
	else: # if a 1 isn't on either side
		return False

m1=[[1, 0, 0],
[0, 1, 0],
[0, 0, 1]]
m2 = [[0, 0, 1],
[0, 1, 0],
[1, 0, 0]]
m3 = [
[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 1, 0, 0],
[0, 0, 0, 1]
]

#m4=[[1, 1, 0],[0, 1, 0],[0, 0, 1]]

print "is_diagonal_matrix(m1)"
print is_diagonal_matrix(m1)
print "is_diagonal_matrix(m2)"
print is_diagonal_matrix(m2)
print "is_diagonal_matrix(m3)"
print is_diagonal_matrix(m3)
#print "is_diagonal_matrix(m4)"
#print is_diagonal_matrix(m4)
