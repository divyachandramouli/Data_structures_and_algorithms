def bubble_sorter(arr):
	n=len(arr)
	for j in range(0,n-1):
		for i in range(0,n-1):
			if (arr[i]>arr[i+1]):
				temp=arr[i]
				arr[i]=arr[i+1]
				arr[i+1]=temp
	return arr

array1=[21,4,1,3,9,20,25,6,21,14]
print(bubble_sorter(array1))