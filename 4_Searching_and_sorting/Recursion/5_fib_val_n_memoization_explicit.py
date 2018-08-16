#Implement memoization explicitly 


fib_cached=[]
def fib(n):
	if n==1:
		value=1
	if n==2:
		value=2
	if n>2:
		value = fib(n-1)+fib(n-2)

	fib_cached[n]=value

	return value

