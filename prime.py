user_input=int(raw_input("enter your no"))
count=2
while count<user_input:
	if user_input%count!=0:
		print count
	count=count+1