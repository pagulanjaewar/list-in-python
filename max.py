list = [1,5,4,6,78,7]
i = 0
max = 0
while i <len(list):
    if max < list[i]:
        max = list[i]
    i = i + 1
print max