def reverse_complement(input_str):
	main_string = list(input_str)
	complement = ""
	for i in main_string:
		if i == "G":
			complement += "T"
		elif i == "T":
			complement += "G"
		elif i == "A":
			complement += "C"
		elif i == "C":
			complement += "A"
	return complement
print(reverse_complement("ATGATG"))