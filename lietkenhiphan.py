cnt = 0
n = 20
x = [0 for i in range(n+1)]

def check(v,k):
	if k == 1:
		return True
	if x[k-1] == 1 and v == 1:
		return False
	return True

def solution():
	global cnt
	cnt += 1
	print('solution ',cnt,': ',x[1:])
	
def Try(k):
	global n
	global x
	global cnt
	
	for v in  range(2):
		if check(v,k):
			x[k] = v
			if k == n:
				solution()
			else:
				Try(k+1)

Try(1)				