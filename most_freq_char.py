def most_freq_char(txt):
	letter_dict = {} # initialize a blank dictionary
	for l in txt: # iterates through the string
		if not letter_dict or l not in letter_dict: # if the dictionary is blank of the letter isn't found
			letter_dict[l] = 1 # add the letter to the dictionary and set its occurences to 1
		else: # if the letter is already in the dictionary
			letter_dict[l] += 1 # increment its occurences by 1

	max_key = txt[0] # set the max letter to the first value in the string
	for c in letter_dict: # iterate through the dictionary (in no particular order)
		if letter_dict[c] > letter_dict[max_key]: # if the current letter occurs more than the current max
			max_key = c # set the most frequent letter to the current letter

	return (max_key, letter_dict[max_key]) # return a tuple of the letter and the number of times it occurs

print "most frequent character in 'aab':"
print most_freq_char("aab")
print "most frequent character in 'abbbccccc!e!f12':"
print most_freq_char("abbbccccc!e!f12")
