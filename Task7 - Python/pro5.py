def unique_list(numbers):
    list1 = []
    for item in numbers :
        if item not in list1:
            list1.append(item)
    return list1


x = []
n = int(input("Enter number of our list elements : "))


for i in range(0, n):
	element = int(input("Enter a number :"))

	x.append(element) 
	
print("your old list is", x)
print("your new list is" , unique_list(x))
print("look up sir")
