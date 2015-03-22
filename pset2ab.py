import heapq
import copy
import collections

dimensions = raw_input().split()
graph = []
body = {}
for x in range(int(dimensions[0])):
	row = list(raw_input())
	graph.append(row)
	for y in range(int(dimensions[1])):
		if (row[y] == 'A'):
			apple = (x,y)

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def getBody (g):
	graph = copy.deepcopy(g)
	for x in range(int(dimensions[0])):
		row = graph[x]
		for y in range(int(dimensions[1])):
			if (row[y] != '.' and row[y] != 'X' and row[y] != 'A'):
				body[row[y]] = (x,y)
	return body

origBody = getBody(graph)
def neighbors(node, g):
	graph = copy.deepcopy(g)
	dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	result = []
	for dir in dirs:
		neighbor = (node[0] + dir[0], node[1] + dir[1])
		if (0 <= neighbor[0] < int(dimensions[0]) and 0 <= neighbor[1] < int(dimensions[1])):
			if (str(graph[neighbor[0]][neighbor[1]]) == '.' or str(graph[neighbor[0]][neighbor[1]]) == 'A' or str(graph[neighbor[0]][neighbor[1]]) == str(dimensions[2])):
				result.append(neighbor)
	return result

def heuristic(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def move_snake(g, newHead):
	graph = copy.deepcopy(g)
	snakeBody = getBody(graph)
	tail = snakeBody[dimensions[2]]
	head = snakeBody['1']
	graph[tail[0]][tail[1]] = '.'
	for x in range(0, int(dimensions[2]) - 1):
		segment = snakeBody[str(int(dimensions[2]) - (x + 1) )]
		graph[segment[0]][segment[1]] = str(int(dimensions[2]) - x)

	graph[newHead[0]][newHead[1]] = '1'
	return graph

def reconstruct_path(came_from, start, goal):
	current = goal
	path = [current]
	while current != start:
		current = came_from[current]
		path.append(current)
	return path

def breadth_first_search(g, start, goal):
	graph = copy.deepcopy(g)
	frontier = Queue()
	frontier.put(start)
	graph_so_far = {}
	graph_so_far[start] = graph
	came_from = {}
	came_from[graph] = None
	found = False

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			found = True
			break

		for next in neighbors(current, graph_so_far[current]):
			if next not in came_from:
				frontier.put(next)
				graph_so_far[next] = move_snake(graph_so_far[current], next)
				came_from[currentGraph] = current
	if (found):
		#return len(reconstruct_path(came_from, start, goal)) - 1
		return
	else:
		return -1


# def a_star_search(g, start, goal):
# 	graph = copy.deepcopy(g)
# 	frontier = PriorityQueue()
# 	frontier.put(start, 0)
# 	came_from = {}
# 	cost_so_far = {}
# 	graph_so_far = {}
# 	visited_count ={}
# 	graph_so_far[start] = graph
# 	came_from[start] = None
# 	cost_so_far[start] = 0
#
# 	while not frontier.empty():
# 		current = frontier.get()
#
#
# 		if current == goal:
# 			break
#
# 		for next in neighbors(current, graph_so_far[current]):
# 			new_cost = cost_so_far[current] + 1
# 			if next in visited_count:
# 				visited_count[next] = visited_count[next] + 1
# 			else:
# 				visited_count[next] = 1
# 			if next not in cost_so_far or new_cost < cost_so_far[next] or len(neighbors(next, graph_so_far[current])) == 1:
# 			#if visited_count[next] < 3:
# 				cost_so_far[next] = new_cost
# 				graph_so_far[next] = move_snake(graph_so_far[current], next)
# 				priority = new_cost + heuristic(goal, next)
# 				frontier.put(next, 1)
# 				came_from[next] = current
# 	if goal in cost_so_far:
# 		return cost_so_far[goal]
# 		#return graph_so_far
# 	else:
# 		return -1
#
# 		#return graph_so_far


head = origBody['1']
print breadth_first_search(graph, head, apple)
#graph2 =[['.','.','3','4','5'], ['X', 'X', '2', '1','.'], ['.','.','.','.','.']]
#print move_snake(graph2,(1,4))
