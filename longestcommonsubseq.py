def input(filename):
	with open(filename,'r') as f:
		[n] = [int(x) for x in f.readline().split()]
		x = [int(x) for x in f.readline().split()]
		[m] = [int(x) for x in f.readline().split()]
		y = [int(x) for x in f.readline().split()]
		return x,y,n,m


x,y,n,m = input('input.txt')
#x,y,n,m = input('lcs.txt')
x[1:] = x[:]
y[1:] = y[:]
print(x,y)
S = [[0 for i in range(m+1)] for j in range(n+1)]
#print(S)

for i in range(1,n+1):
	for j in range(1,m+1):
		if x[i] == y[j]:
			S[i][j] = S[i-1][j-1] + 1
		else:
			if S[i-1][j] > S[i][j-1]:
				S[i][j] = S[i-1][j]
			else:
				S[i][j] = S[i][j-1]
print(S)
ans = S[n][m]
print(ans)		
f = open('result.txt','w')
f.write(str(ans))
f.close()		
		