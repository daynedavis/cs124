import sys

def meetConstraints (a):
	if a >= 1 and a <= 1000:
		return True
a, b = map(int,raw_input().split())
if meetConstraints(a) and meetConstraints(b):
	print a + b
