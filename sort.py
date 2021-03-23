def input(filename):
	n = 0
	a = []
	with open(filename,'r') as f:
		cnt = 0
		for line in f:
			if cnt == 0:
				n = int(line)
			elif cnt == 1:
				a = [int(x) for x in line.split()]
			cnt = cnt + 1
	return n, a


def swap(i,j):
	global a
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	
def selectionSort():
	for k in range(n):
		min = k
		for j in range(k+1,n):
			if a[min] > a[j]:
				min = j
		swap(k,min)
		#print('B',k,' a = ',a)

def insertionSort():
	for k in range(1,n):
		last = a[k]
		j = k
		while j > 0 and a[j-1] > last:
			a[j] = a[j-1]
			j = j - 1
		a[j] = last

def merge(L,M,R):
	global a,ta
	i = L
	j = M+1
	for k in range(L,R+1):
		#print('merge i = ',i,' k = ',k,' j = ',j,' L = ',L,' M = ',M,' R = ',R, ' len ta = ', len(ta))
		if i > M:
			ta[k] = a[j]
			j = j + 1
		elif j > R:
			ta[k] = a[i]
			i = i + 1
		else:
			if a[i] < a[j]:
				ta[k] = a[i]
				i += 1
			else:
				ta[k] = a[j]
				j += 1
				
	a[L:R+1] = ta[L:R+1]
	

def mergeSortR(L,R):
	if L < R:
		M = (L+R)//2
		mergeSortR(L,M)
		mergeSortR(M+1,R)
		merge(L,M,R)

def mergeSort():
	global ta
	ta = [0 for i in range(n)]
	mergeSortR(0,n-1)
	
ta = []
		
n,a = input('input.txt')
print(n,a)	
mergeSort()
print('after sort, a = ',a)
f = open('result.txt','w')
for i in a:
	f.write(str(i) + ' ')
