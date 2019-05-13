user_input1=int(raw_input("enter your no"))
user_input2=int(raw_input("enter your no"))
user_input3=int(raw_input("enter your no"))
if (user_input1>user_input2 and user_input1>user_input3):
	print user_input1
elif user_input2>user_input3 and user_input2>user_input1:
	print user_input2
else:
	print user_input3	
