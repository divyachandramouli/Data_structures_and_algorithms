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


arr1=[2,6,12]
arr2=[1,11,100]
print(merge(arr1,arr2))