row=1

N=int(raw_input("enter your no"))
space=N/2
U_size=N/2+1 #size of upper half trangle
#upper half trangle
while (row<=U_size):
    column=1
    
    #left part
    while column<=space:
        print " ",
        column=column+1
    i=N-(2 * space)
    #Middle part
    while i>0:
        print "*",
        column=column+1
        i=i-1
    print " " 
    space=space-1
    row= row+1
    
#Lower half trangle    
space=1
while row<=N:
    
    column=1
    
    #left part
    while column<=space:
        print " ",
        column=column+1
        
    i=N-(2 * space)
    
    #Middle part
    while i>0:
        print "*",
        column=column+1
        i=i-1
    print " "
    space=space+1
    row=row+1