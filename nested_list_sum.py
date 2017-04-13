def nested_list_sum(nested_list):
	sum = 0 # initialize the sum to 0
	for l in nested_list: # iterate through the list
		if isinstance(l, list): # if the current instance is another list
			sum += nested_list_sum(l) # add the recursive call on the list to the overall sum
		else: # if the current item in the list is not another list
			sum += l # add the value to the sum

	return sum

print "nested_list_sum([1, 2])"
print nested_list_sum([1, 2])
print "nested_list_sum([[1], 2])"
print nested_list_sum([[1], 2])
print "nested_list_sum([[[[1, [[[[2]]]]], 3]]])"
print nested_list_sum([[[[1, [[[[2]]]]], 3]]])
print "nested_list_sum([[1, [[[[2, [3]]], 4]], 5], 6, 7])"
print nested_list_sum([[1, [[[[2, [3]]], 4]], 5], 6, 7])
