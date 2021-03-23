cnt = 0
def move(n,A,B,C):
	global cnt
	if n == 1:
		cnt += 1
		print('Step ',cnt,': move ',A,' -> ',B)
	else:
		move(n-1,A,C,B)
		move(1,A,B,C)
		move(n-1,C,B,A)
	
move(3,'A','B','C')	