def sorting(z):
    z.sort()
  

def firstandlast(arr, n, x):
	first = -1
	last = -1
	for i in range(0, n):
		if (x != arr[i]):
			continue
		if (first == -1):
			first = i
		last = i

	if (first != -1):
		print("First Occurrence is = ", first," And Last Occurrence is = ", last)
	else:
		print("Not Found")


z =[8,7,10,8,8,5,7]
sorting(z)
print("your array sorted to :", z)
n = len(z)
x = 8
firstandlast(z, n, x)
