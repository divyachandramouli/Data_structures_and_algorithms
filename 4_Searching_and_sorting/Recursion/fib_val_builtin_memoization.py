#Implement memoization explicitly 

from functools import lru_cache

@lru_cache()

def fib(n):
	if n==1:
			return 1
	if n==2:
			return 2
	if n>2:
			return fib(n-1)+fib(n-2)

for i in range(1,1001):
	print(i,':',fib(i))