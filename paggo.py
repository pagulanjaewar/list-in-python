user_input = int(raw_input("enter your no"))
raw=1
while raw<=user_input:
	column = 1
	while column<=raw:
		print "*",
		column = column+1
	print "\n"
	raw=raw+1