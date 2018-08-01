#Return the value of fib seq given the pos

def get_fib_val(pos):
	if (pos==0):
		return 0
	if (pos==1):
		return 1
	first=0
	second=1
	next=first+second
	for i in range(2,pos):
		first=second
		second=next
		next=first+second
	return next

print(get_fib_val(6))