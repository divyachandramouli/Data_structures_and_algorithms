# Function to merge two  arrays in sorted order

def merge(a,b):
	a_idx=0
	b_idx=0
	c=[]
	while(a_idx<=len(a)-1 and b_idx<=len(b)-1):
		if (a[a_idx]<b[b_idx]):
			c.append(a[a_idx])
		else:
			c.append(b[b_idx])
	if (a_idx==len(a)):
		c.extend(b[b_idx:])
	else:
		c.extend(a[a_idx:])
	return c


	