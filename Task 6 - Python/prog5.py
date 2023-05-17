def minDistance(a):
	x = dict()
	minDistance = 1000
	previousIndex = 0
	currentIndex = 0

	for i in range(len(a)):

		if a[i] in x:
			currentIndex = i
			previousIndex = x[a[i]]
			minDistance = min((currentIndex - previousIndex), minDistance)
		x[a[i]] = i

	if minDistance == 1000:
		return -1
	return minDistance

a1 = [2, 5, 3, 4, 5 , 2]
print(minDistance(a1))