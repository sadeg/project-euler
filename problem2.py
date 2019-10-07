#Even Fibonacci numbers
#Problem 2
'''

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''
import logging


logging.basicConfig(level = logging.DEBUG)

def fib(n):
	if (n == 0):
		return 1
	elif (n == 1):
		return 1
	else:
		return (fib(n-2) + fib(n-1))

i = 1
while(True):
	if(fib(i) >= 4000000):
		loggign.debug("fib({i}) = {f}".format(i = i, f = fib(i)))
		break
	else:
		i -= 1
