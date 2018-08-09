# Function to merge two sorted arrays in sorted order

def merge(a,b):
	a_idx=0
	b_idx=0
	c=[]
	while(a_idx<=len(a)-1 and b_idx<=len(b)-1):
		if (a[a_idx]<b[b_idx]):
			c.append(a[a_idx])
			a_idx=a_idx+1
		else:
			c.append(b[b_idx])
			b_idx=b_idx+1
	if (a_idx==len(a)):
		c.extend(b[b_idx:])
	else:
		c.extend(a[a_idx:])
	return c

def merge_sort(arr):
	# A list of zero or one element is already sorted
	if(len(arr)<=1):
		return arr
	# Split the list in half and call merge sort recursively on each half
	left,right=merge_sort(arr[0:len(arr)//2]), merge_sort(arr[len(arr)//2:])
	#Merge the now sorted sublists
	return merge(left,right)

'''
arr1=[2,6,12]
arr2=[1,11,100]
print(merge(arr1,arr2))
'''
arr1=[101,65,42,2,65,72,11,5,1,89,10,3]
print(merge_sort(arr1))

"Time Complexity in best, worst and avg case: O(nlogn)"
"Time complexity is same in all 3 cases because merge_sort always divides "
"array in half and takes linear time to merge the two halves"
"SPace complexity: O(n) - extra space to copy the merged array"

