start = 3,2
adjacent = []
# adjacent= zip([x for x in xrange(-1, 2)],[y for y in xrange(1, -2, -1)])

for x in xrange(-1, 2):
	for y in xrange(1, -2, -1):
		adjacent.append((start[0] + x, start[1] + y))


print(adjacent)