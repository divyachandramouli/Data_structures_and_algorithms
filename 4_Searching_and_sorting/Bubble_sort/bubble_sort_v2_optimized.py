# Optimized implementation of bubble sort to stop if no more swaps are required

def bubble_sorter(arr):
	n=len(arr)
	i=0
	for j in range(0,n):
		swapped=False
		for i in range(0,n-j-1):
			#In the  jth iteration, last j elements have bubbled up so leave them
			if (arr[i]>arr[i+1]):
				arr[i],arr[i+1]=arr[i+1],arr[i]
				swapped=True
		# If no two elements were swapped
        # by inner loop, then break
		if swapped==False:
			break
				
	return arr

array1=[21,4,1,3,9,20,25,6,21,14]
print(bubble_sorter(array1))