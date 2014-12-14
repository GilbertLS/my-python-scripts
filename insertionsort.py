myArray = [5,4,3,2,1]

def insertionSort(A, length):

	if length <= 1:
		return A
	else:
		A = insertionSort(A, length-1)

		for i in range(0,length-1):
			if A[length-1] <= A[i]:
				for j in range(i, length-1):
					key = A[j]
					A[j] = A[length-1]
					A[length-1] = key
				break

	return A

print(insertionSort(myArray, len(myArray)))
