first_line = map(int, raw_input().split())
breaks = map(int, raw_input().split())
num_breaks = first_line[0]
length = first_line[1]

def splitter(length, breaks):
	if len(breaks) == 0:
		return [0,[]]
	min_cut_order = []
	min_time = 1000000000
	for k in breaks:
		left_break = [ x for x in breaks if x < k]
		right_break = [ x - k for x in breaks if x > k]
		left_time = splitter(k, left_break)
		right_time = splitter(length-k, right_break)
		time = length + left_time[0] + right_time[0]
		cut_order = [k] + left_time[1] + [x + k for x in right_time[1]]
		if time < min_time:
			min_time = time
			min_cut_order = cut_order
	return (min_time, min_cut_order)

print splitter(length, breaks)[0]
