def solve(x):
	largest = x[0]
	lowest = x[0]
	largest2 = x[0]
	lowest2 = x[0]
	for i in x[1:]:	
		if i > largest:
			largest2 = largest
			largest = i
		elif largest2 != largest and largest2 < i:
			largest2 = i
		if i < lowest:
			lowest2 = lowest
			lowest = i
		elif lowest2 != lowest and lowest2 > i:
			lowest2 = i
			
	print("Largest number is:", largest)
	print("Second largest number is:", largest2)
	print("Smallest number is:", lowest)
	print("Second smallest number is:", lowest2)
x = [10, 5, 99]
solve(x)

