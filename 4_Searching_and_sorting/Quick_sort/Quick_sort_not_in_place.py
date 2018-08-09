#Implementation of quick sort ( not in place) - uses random pivot
from random import randint
def quicksort(a):
	if len(a)<=1:
		return a
		smaller,equal,larger=[],[],[]
		pivot=a[randint(0,len(a)-1)]
		for x in a:
			if x<pivot:
				smaller.append(x)
			elif x>pivot:
				larger.append(x)
			else:
				equal.append(x)
		return quicksort(smaller)+equal+quicksort(larger)

arr1=[8,3,1,7,0,10,2]
print(quicksort(arr1))

		