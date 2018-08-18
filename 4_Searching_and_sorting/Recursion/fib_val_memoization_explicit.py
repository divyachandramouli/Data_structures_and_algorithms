#Implement memoization explicitly 


fib_cached={}
def fib(n):
	#If we already have the cached value return it
	if n in fib_cached:
		return fib_cached[n]
	else:
		#Compute the nth term, cache it, then return it
		if n==1:
			value=1
		if n==2:
			value=2
		if n>2:
			value = fib(n-1)+fib(n-2)

		fib_cached[n]=value

		return value

for i in range(1,1001):
	print(i,':',fib(i))