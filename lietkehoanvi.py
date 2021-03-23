n = 10   
cnt = 0
visited = [False for v in range(n+1)]
x = [0 for i in range(n+1)]

def check(v,k):
	return visited[v] == False
def solution():
	global cnt
	cnt += 1
	print(cnt,': ',x[1:])
	
def Try(k):
	for v in range(1,n+1):
		if check(v,k):
			x[k] = v
			visited[v] = True #update visited
			
			if k == n:
				solution()
			else:
				Try(k+1)
			
			visited[v] = False #recover when backtracking

Try(1)			