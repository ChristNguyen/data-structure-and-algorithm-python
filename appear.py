import random as rd

def input(filename):
	a = []
	b = []
	K = 0
	with open(filename,'r') as f:
		for line in f:
			a = [int(x) for x in line.split()]
			break
		for line in f:
			[K] = [int(x) for x in line.split()]
			break
		for line in f:
			b = [int(x) for x in line.split()]
	return a,K,b

def genData(filename,n,K):
	f = open(filename,'w')
	s = ''
	for i in range(n):
		x = rd.randint(1,n)
		s = s + str(x) + ' '
	f.write(s + '\n')
	f.write(str(K) + '\n')
	s = ''
	for i in range(K):
		x = rd.randint(1,2*n)
		s = s + str(x) + ' '
	f.write(s)
	f.close()
	
#genData('appear.in5',100000,100000)	
#a,K,b = input('appear.in5')
#f = open('appear.ou2','w')
a,K,b = input('input.txt')
f = open('result.txt','w')

a.sort()

#print(a,K,b)	

def bSearch(L,R,x):
	if L > R:
		return 0
	if L == R:
		if a[L] == x:
			return 1
		else:
			return 0
	m = (L+R)//2
	if a[m] == x:
		return 1
	else:
		if a[m] < x:
			return bSearch(m+1,R,x)
		else:
			return bSearch(L,m-1,x)

for i in range(len(b)):
	rs = bSearch(0,len(a)-1,b[i])
	f.write(str(rs) + '\n')
	#print(rs)
	
f.close()
	