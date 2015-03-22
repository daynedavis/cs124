firstLine = raw_input()
ids = raw_input().split()
# firstLine = '5'
# ids = ['2', '2', '4', '1', '2']
# ids = ['2', '2', '4', '1', '2', '2', '4', '1', '2']
# ids = ['2', '2', '2', '2', '1', '1', '1', '1', '1']

dictLeftToRight = {}
dictRightToLeft = {}
arrayLeftToRight = []
arrayRightToLeft = []

for x in range(len(ids)):
	if (ids[x] in dictLeftToRight):
		dictLeftToRight[ids[x]] += 1
		arrayLeftToRight.append(dictLeftToRight[ids[x]])
	else:
		dictLeftToRight[ids[x]] = 1
		arrayLeftToRight.append(1)
	if (ids[len(ids) - 1 - x] in dictRightToLeft):
		dictRightToLeft[ids[len(ids) - 1 - x]] += 1
		arrayRightToLeft.insert(0,dictRightToLeft[ids[len(ids) - 1 - x]])
	else:
		dictRightToLeft[ids[len(ids) - 1 - x]] = 1
		arrayRightToLeft.insert(0,1)

def helper(L, R):
	inversions = 0
	y = len(R) - 1
	for x in range(len(L)):
		while y >= 0:
 			if L[len(L) - 1 - x] > R[y]:
				inversions += y + 1
				break
			else:
				y -= 1
	return inversions

def recur(L,R):
	half = len(L)/2
	if len(L) < 2 or len(R) < 2:
		return 0
	else:
		LL = L[:half]
		LR = L[half:]
		RL = R[:half]
		RR = R[half:]
		inversions = recur(LL,RL)
		inversions += recur(LR, RR)
		LL.sort()
		RR.sort()
		inversions += helper(LL,RR)
		return inversions

print recur(arrayLeftToRight, arrayRightToLeft)
