def input(filename):
	with open(filename, 'r') as f:
		[n]  = [int(x) for x in f.readline().split()]
		x = [int(x) for x in f.readline().split()]
		return x,n

def maxIncrease(a, n):
    print('maxIn, n = ',n)
    s = [0 for i in range(n)]
    s[0] = a[0]
    ans = s[0]
    trace = [-1 for i in range(n)] # trace[i] = j: la chi so j ma S[i] duoc xay dung tu S[j]
    max_index = 0
    for i in range(1, n):
        s[i] = a[i]
        for j in range(i):
            if a[j] < a[i] and s[i]< s[j] + a[i]:
                s[i] = s[j] + a[i]
                trace[i] = j
        #ans = max(ans, s[i])
        if ans < s[i]:
            ans = s[i]
            max_index = i
			
    return ans, trace, max_index



a,n =input('maxincseq.txt')
print('n = ',n,' a = ',a)
##result = maxIncrease([3, 8, 10, 1, 5, 7, 9], 7)
result, trace, max_index = maxIncrease(a, n)
f = open('result.txt', 'w')
f.write(str(result))
f.close()
print(result)

# Truy vet dua vao trace va max_index
print('day ket qua:')
i = max_index
while trace[i] >= 0:
	print(a[i])
	i = trace[i]
print(a[i])	
	
