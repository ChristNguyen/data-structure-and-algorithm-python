import numpy as np

x = np.array([[0 for i in range(9)] for j in range(9)])

with open("sudoku.txt","r") as f:
	a = [[int(v) for v in line.split()] for line in f] 
a = np.array(a)	
print('init config')
print(a)		

x[:] = a[:]

sol = np.array(x)

found = False

markRow = np.array([[False for r in range(9)] for v in range(10)])
markCol = np.array([[False for c in range(9)] for v in range(10)])
markSquare = np.array([[[False for I in range(3)] for J in range(3)] for v in range(10)])

for r in range(9):
	for c in range(9):
		if x[r][c] > 0:
			v = x[r][c]
			markRow[v][r] = True
			markCol[v][c] = True
			markSquare[v][r//3][c//3] = True
			
def check(v,r,c):
	return (not markRow[v][r]) and (not markCol[v][c]) and (not markSquare[v][r//3][c//3]) 
	
def solution():
	global found
	found = True
	sol[:] = x[:]
	print('FOUND solution')
	#print(x)
	#print('----------------------------')
	
def Try(r,c): #try all values for x[r][c]
	#print('Try(',r,',',c,'),a[r][c] = ',a[r][c])
	global found
	if found == True:
		return

	if a[r][c] > 0:
		if r == 8 and c == 8:
			solution()
		else:
			if c == 8:
				Try(r+1,0)
			else:
				Try(r,c+1)
		return

		
	for v in range(1,10):
		#print('Try(',r,c,') v = ',v,' check = ',check(v,r,c))
		if check(v,r,c):
			x[r][c] = v
			#print('Try(',r,c,') assign ',v)
			#print(x)
			markRow[v][r] = True # v appears on row r
			markCol[v][c] = True # v appears on column c
			markSquare[v][r//3][c//3] = True#r = 0,1,2 -> I = 0; r = 3,4,5 -> I = 1; r = 6,7,8 -> I = 2
			if r == 8 and c == 8:
				solution()
			else:
				if c == 8:
					Try(r+1,0)
				else:
					Try(r,c+1)
			markRow[v][r] = False # v appears on row r
			markCol[v][c] = False # v appears on column c
			markSquare[v][r//3][c//3] = False#r = 0,1,2 -> I = 0; r = 3,4,5 -> I = 1; r = 6,7,8 -> I = 2
			x[r][c] = 0

Try(0,0)
print('solution:')
print(sol)
