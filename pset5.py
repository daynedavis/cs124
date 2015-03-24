first_line = map(int, raw_input().split())
breaks = map(int, raw_input().split())
num_breaks = first_line[0]
length = first_line[1]

def splitter(l, breaks):
	if len(breaks) == 0:
		return 0
	min_cut_order = []
	min_time = 1000000000
	for index, k in enumerate(breaks):
		left_break = breaks[:index]
		right_break = [ x - k for x in breaks if x > k]
		left_time = splitter(k, left_break)
		right_time = splitter(l-k, right_break)
		time = l + left_time + right_time
		if time < min_time:
			min_time = time
	return min_time

print splitter(length, breaks)
