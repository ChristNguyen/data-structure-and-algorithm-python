import random as rd

def input(filename):
	with open(filename,'r') as f:
		n = 0
		a = []
		for line in f:
			n = int(line)
			break
		for line in f:
			a = [int(x) for x in line.split()]
			break
		return n,a

def genData(filename,n):
	f = open(filename,'w')
	f.write(str(n) + '\n')
	s = ''
	for i in range(n):
		x = 1000-rd.randint(0,2000)
		s = s + str(x) + ' '
	f.write(s)
	f.close()

def maxLeft(L,R):
	ans = a[R]
	S = a[R]
	for i in range(R-1,L-1,-1):
		S = S + a[i]
		ans = max(ans,S)
	return ans

def maxRight(L,R):
	ans = a[L]
	S = a[L]
	for i in range(L+1,R+1):
		S = S + a[i]
		ans = max(ans,S)
	return ans
	
def maxsubseq(L,R):
	if L == R:
		return a[L]
	m = (L+R)//2
	mL = maxsubseq(L,m)
	mR = maxsubseq(m+1,R)
	mLR = maxLeft(L,m) + maxRight(m+1,R)
	ans = max(max(mL,mR),mLR)
	return ans
	
n,a = input('input.txt')
f = open('result.txt','w')
ans = maxsubseq(0,n-1)
print(ans)
f.write(str(ans))
f.close()