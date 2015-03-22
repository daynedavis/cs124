import heapq
import copy
import collections

dimensions = raw_input().split()
graph = []
origBody = []
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(int(dimensions[2])):
	origBody.append(0)
blankSnake = copy.deepcopy(origBody)

for x in range(int(dimensions[0])):
	row = list(raw_input())
	for y in range(int(dimensions[1])):
		if (row[y] == 'A'):
			apple = (x,y)
		elif (row[y] != '.' and row[y] != 'X' and row[y] != 'A'):
			origBody[int(row[y]) - 1] = (x,y)
			row[y] = '.'
	graph.append(row)

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

def neighbors(node, body):
	b = copy.deepcopy(body)
	result = []
	for dir in dirs:
		neighbor = (node[0] + dir[0], node[1] + dir[1])
		if (0 <= neighbor[0] < int(dimensions[0]) and 0 <= neighbor[1] < int(dimensions[1])):
			if ((str(graph[neighbor[0]][neighbor[1]]) == '.' or str(graph[neighbor[0]][neighbor[1]]) == 'A')  and (((neighbor in b) == False) or b[int(dimensions[2]) - 1] == neighbor ) ):
				result.append((move_snake(b,neighbor), neighbor))
	return result


def move_snake(b, newHead):
	blank = []
	blank.append(newHead)
	for x in range(1, int(dimensions[2])):
		blank.append(b[x-1])
	return blank

def breadth_first_search(b, start, goal):
	body = copy.deepcopy(b)
	frontier = Queue()
	frontier.put([body, start, 0])
	graph_so_far = {}
	counter = 1
	graph_so_far[str(origBody)] = 1
	found = False

	while not frontier.empty():
		current = frontier.get()
		currentCount = current[2]
		currentGraph = current[0]
		current = current[1]

		if current == goal:
			found = True
			break

		for next in neighbors(current, currentGraph):
			if str(next[0]) not in graph_so_far:
				graph_so_far[str(next[0])] = 1
				frontier.put([next[0], next[1], currentCount + 1])
	if (found):
		return currentCount
	else:
		return -1


head = origBody[0]
print breadth_first_search(origBody, head, apple)
