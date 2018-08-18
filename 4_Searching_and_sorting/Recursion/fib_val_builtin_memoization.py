#Implement memoization explicitly 

from functools import lru_cache #Least Recently Used Cache - a decorator
#By default it caches 128 most recent function calls - specify #values to cache 

@lru_cache(maxsize=1000)

def fib(n):
#Check that the input is a positive integer
	if type(n) != int:
		raise TypeError ("n must be a positive integer")
# No fraction values are accepted 
	if n<1:
		raise TypeError ("n must be a positive integer")
	if n==1:
			return 1
	if n==2:
			return 2
	if n>2:
			return fib(n-1)+fib(n-2)

for i in range(1,1001):
	print(i,':',fib(i))