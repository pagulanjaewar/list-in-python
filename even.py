user_input=int(raw_input("enter no"))
count=0
sum1=0
while count<user_input:
	if count%2==0:
		sum1=sum1+count
	count=count+1
print sum1