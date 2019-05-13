list1=[0,1,4,1,1]
count=1
sum1=0
power=0
while count<len(list1):
	binary=list1[-count]
	if binary==0 or binary==1:
		multiple=list1[count]*2**power
		sum1=sum1+multiple
		power=power+1
		count=count+1
	else:
		break
print sum1
	
	# elif binary!=0 and binary!=1:
	# 	continue
	# print sum1
	 


