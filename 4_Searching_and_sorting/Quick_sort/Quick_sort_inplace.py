#Quick Sort Algorithm - in-place

def partition(A,left,right):
	pivot=A[right]
	Pidx=left-1
	for j in range(left,right):
		if(A[j]<=pivot):
			Pidx=Pidx+1
			A[j],A[Pidx]=A[Pidx],A[j]
	A[Pidx+1],A[right]=A[right],A[Pidx+1]	
	return Pidx+1

def quicksort(A,start,end):

	if(start<end):
		p=partition(A,start,end)
		quicksort(A,start,p-1)
		quicksort(A,p+1,end)	
	

arr=[8,3,1,7,0,10,2]
left=0
right=len(arr)-1
print(arr)
(quicksort(arr,left,right))
print(arr)
'''
def quicksort(A,start,end):
	if len(A)<=1:
		return A
	if(start<end):
		p=partition(A,start,end)
		quicksort(A,start,p-1)
		quicksort(A,p+1,end)
		'''


