#Generate fibonacci seq with index as input - Iterative

def getfib(pos):
	
	fib=[0,1]
	first=fib[0]
	second=fib[1]
	if (pos==0):
		return fib[0]
	if (pos==1):
		return fib
	for i in range (2,pos+1):
		next=first+second
		first=second
		second=next
		fib.append(next)
	return fib


print(getfib(2))
