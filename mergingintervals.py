
def mergeIntervals(arr):
	arr.sort()
	j = 0

	for i in range(1, len(arr)):
		if (arr[j][1] >= arr[i][0]):
			arr[j][1] = max(arr[j][1], arr[i][1])
		else:
			j = j + 1
			arr[j] = arr[i]

	print("The Merged Intervals are :", end=" ")
	for i in range(j+1):
		print(arr[i], end=" ")


arr = [[8,9],[1,2],[2,4],[4,7],[1,5],[3,4]]
mergeIntervals(arr)
