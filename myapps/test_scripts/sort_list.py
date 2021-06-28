mylist = [0.1,2,3,0.5]

def smallestnumber(list):
    list.sort()
    return list[0]

print(smallestnumber(mylist))

def largestnumber(list):
    list.sort()
    return list[-1]

print(largestnumber(mylist))
