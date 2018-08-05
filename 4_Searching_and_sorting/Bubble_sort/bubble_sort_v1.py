# Implementation of bubble sort 

def bubble_sorter(arr):
	n=len(arr)
	i=0
	for j in range(0,n-1):
		for i in range(0,n-i-1):
			#In the  ith iteration, last i elements have bubbled up
			if (arr[i]>arr[i+1]):
				
				arr[i],arr[i+1]=arr[i+1],arr[i]
				
	return arr


array1=[21,4,1,3,9,20,25,6,21,14]
print(bubble_sorter(array1))

" Average and worst case time complexity: O(n*n)"
" The above algorithm always runs O(n^2) time even if the array is sorted."
"It can be optimized by stopping the algorithm if inner loop didn't cause any swap"