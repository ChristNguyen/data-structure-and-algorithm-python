def input(filename):
	with open(filename,'r') as f:
		for line in f:
			[x,n] = [int(x) for x in line.split()]
			return x,n

P = int(1e9+7)
def exp(x,n):
	if n == 1:
		return x%P
	n1 = n//2
	tmp = exp(x,n1)
	tmp = (tmp*tmp)%P
	if n%2 == 1:
		tmp = (tmp*x)%P
	return tmp
	
x,n = input('input.txt')
print(x,n)
ans = exp(x,n)
print(ans)
f = open('result.txt','w')
f.write(str(ans))		