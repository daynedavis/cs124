import math
import copy
dimensions = int(raw_input())

statements = []

for x in range(0,dimensions):
	statements.append(raw_input().split())

matrix = [[0 for x in range(dimensions)] for x in range(dimensions)]
identity = [[0 for x in range(dimensions)] for x in range(dimensions)]

for x in range(0,dimensions):
	for y in range(0,len(statements[x])):
		matrix[x][int(statements[x][y])] = 1
orig = copy.deepcopy(matrix)
for x in range(0,dimensions):
	identity[x][x] = 1

def matrix_multiply(A, B):
        n = len(A)
        m = len(A[0])
        p = len(B[0])
        C = [[0]*p for i in range(n)]
        for i in range(n):
                ai = A[i]
                ci = C[i]
                for k in range(m):
                        bk = B[k]
                        a = ai[k]
                        for j in range(p):
                                ci[j] += min(300, a * bk[j])
        return C

def matrix_subtract(b, y):
	x = copy.deepcopy(b)
	for c in range(len(x)):
		for b in range(len(x)):
			if y[c][b] >= 1:
				x[c][b] = x[c][b] - y[c][b]
	return x

def matrix_add(b, y):
	x = copy.deepcopy(b)
	for c in range(len(x)):
		for b in range(len(x)):
			x[c][b] = x[c][b] + y[c][b]
	return x

def matrix_scale(b, y):
	x = copy.deepcopy(b)
	for c in range(len(x)):
		for b in range(len(x)):
			x[c][b] = x[c][b] * y
	return x

def square(a, b):
	c = a
	for i in range(b):
		c = matrix_multiply(c,c)
	return c

def efficientPower(b, p):
	bins = bin(dimensions - 1)
	ex = map(int, list(bins[2: len(bins)])[::-1])
	squared = identity

	for x in range(len(ex)):
		if x != 0 and ex[x] == 1:
			squared = matrix_multiply(squared, square(b, x))
		if x == 0 and ex[x] == 1:
			squared = matrix_multiply(squared, b)
	return squared

def matrix_compare(b, y):
	x = copy.deepcopy(b)
	for c in range(len(x)):
		for b in range(len(x)):
			if x[c][b] > 0 and y[c][b] > 0:
				x[c][b] = 0
			elif x[c][b] > 0:
				x[c][b] = 1
	return x

first = efficientPower(matrix_add(orig, identity), dimensions - 1)
second = matrix_scale(orig, dimensions -1)
new = matrix_subtract(matrix_subtract(first, second), identity)
finished = matrix_compare(orig, new)

for c in range(len(finished)):
	row = ''
	for b in range(len(finished)):
		if finished[c][b] > 0:
			row += str(b) + ' '
	print row
