# x1 + x2 + . . . + xn = M
n = 10
M = 15
x = [0 for i in range(n+1)]
T = 0

def check(v,k):
	global T,n,M
	if k < n:
		return T + v < M
	else:
		return T + v == M
	
def solution():
	print(x[1:])
	
def Try(k):
	global T
	# da biet x(1), x(2), ..., x(k-1)
	# for v = 1 to M - T - (n-k) do
	for v in range(1,M-T-(n-k)+ 1):
		if check(v,k):
			x[k] = v
			T = T + v # update T incrementally
			if k == n:
				solution()
			else:
				Try(k+1)
			T = T - v #recover when backtracking	

Try(1)