#import numpy as np

def match(a,b):
	if a == '(' and b == ')':
		return True
	if a == '[' and b == ']':
		return True
	if a == '{' and b == '}':
		return True
	
	return False
	
def check(e):
	stack = []
	for i in range(len(e)):
		if e[i] == '(' or e[i] == '[' or e[i] == '{':
			stack.append(e[i])
		else:
			if len(stack) == 0:
				return False
			x = stack.pop()
			ok = match(x,e[i])
			#print('match(',x,',',e[i],' = ',ok)
			if not ok:
				return False
	return len(stack) == 0			

def std(s):
	ns = ''
	for i in range(len(s)):
		if s[i] == '(' or s[i] == ')' or s[i] == '[' or s[i] == ']' or s[i] == '{' or s[i] == '}':
			ns = ns + s[i]
	return ns
	
def input():
    with open('input.txt','r') as f:
        s = str(f.readline())		
    return s.strip()

f = open('result.txt', 'w')

s = input()
'''
s = '(  )[]{ }  '
s = std(s)
print('std s = ',s)
'''

ok = check(s)
if ok:
	result = 1
else:
	result = 0
result
print(ok)


f.write(str(result))
	
#ok = check('()[]{[(){}]}')		
#print(ok)