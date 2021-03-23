import numpy as np

sz = 100
M = np.zeros((sz,sz),dtype='int64')

def f(n):
    if n == 1:
        return 1
    return f(n-1) + n

def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def C(k,n):
	#global M
	if k == 0 or k == n:
		M[k][n] = 1
	else:
		if M[k][n] == 0:
			M[k][n] = C(k-1,n-1) + C(k,n-1)
	
	return M[k][n]

	
print(C(50,80))