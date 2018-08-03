def bubble_sorter(arr)
	n=len(arr)
	for i in range(0,n):
		if (arr[i]>arr[i+1]):
			temp=arr[i]
			arr[i]=arr[i+1]
			arr[i+1]=temp
	return arr

array1=[21,4,1,3,9,20,25,6,21,14]
print(bubble_sorter(array1))