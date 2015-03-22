firstLine = raw_input().split()

N = firstLine[0]
M = firstLine[1]
L = firstLine[2]

N = int(N)
inputRows = int(M) + int(L)

rounds = []
for i in range(inputRows):
	rounds.append(raw_input().split())
set = {}
contributions = 0

class makeSet:
	def __init__(self, name):
		self.parent = self
		self.name = name
		self.score = 1
		self.highest = self

def find(x):
	b = x
	while b.parent != b.parent.parent:
		x.score += b.parent.score
		b = b.parent
	x.parent = b.parent
	return b.parent


def union(x,y):
	xRoot = find(x)
	yRoot = find(y)
	yHigh = highest(y)
	xHigh = highest(x)
	yRoot.highest = xHigh
	xRoot.parent = yHigh

def highest(x):
	if x.parent == x:
		return x.highest
	else:
		return highest(x.parent)

def contribute(x):
	score = x.score
	while x != x.parent:
		score += x.parent.score
		x = x.parent
	return score

for i in range(N):
	set[str(i)] = makeSet(str(i))

for i in range(len(rounds)):
	a = set[rounds[i][0]]

	if len(rounds[i]) == 1:
		contributions = contributions + contribute(a)
	else:
		b =set[rounds[i][1]]
		if find(a) != find(b):
			union(a,b)

print contributions
