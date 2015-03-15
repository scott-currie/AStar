import random

#--Constants
MAP_WIDTH = 30
MAP_HEIGHT = 30
NUM_BARRIERS = int(.6 * (MAP_WIDTH * MAP_HEIGHT))	#Specified percentage of total number of spaces.

#--Objects
map = {}
start = (-1,-1)
goal = (-1,-1)
open_list = []
closed_list = []

def init_map():
	'''Init dict map with empty spaces. Key is tuple representing x,y coords.'''
	for x in xrange(MAP_WIDTH):
		for y in xrange(MAP_HEIGHT):
			map[(x,y)] = '.'

def init_barriers():
	'''Randomly set num_barriers number of elements in dict map with '#' to represent barriers.'''
	num_barriers = NUM_BARRIERS
	while num_barriers > 0:
		randx = random.randint(0, MAP_WIDTH - 1)
		randy = random.randint(0, MAP_HEIGHT - 1)
		if map[(randx,randy)] == '.':
			map[(randx,randy)] = '#'
			num_barriers -= 1

def init_start():
	'''Randomly place start, a tuple with x,y coords'''
	global start
	while start == (-1, -1):
		randx = random.randint(0, MAP_WIDTH - 1)
		randy = random.randint(0, MAP_HEIGHT - 1)
		if map[(randx, randy)] == '.' and goal != (randx, randy):
			start = (randx, randy)

def init_goal():
	'''Randomly place goal, a tuple of x,y coords'''
	global goal
	while goal == (-1, -1):
		randx = random.randint(0, MAP_WIDTH - 1)
		randy = random.randint(0, MAP_HEIGHT - 1)
		if map[(randx, randy)] == '.' and start != (randx, randy):
			goal = (randx, randy)

def check_path_to_goal():
	'''Flood fill map to see if any path exist from start to goal. 
	   Returns true if path exists, else returns false'''
	global start, goal
	checked = [start]
	cont = True
	while cont:
		new_spaces = []
		for space in checked:
			for col in xrange(-1, 2):
				for row in xrange(-1, 2):
					#--Create potential space
					to_add = (space[0] + col, space[1] + row)
					#--Check if potential space out of bounds
					if (to_add[0] >= 0 and to_add[0] < MAP_WIDTH) and (to_add[1] >= 0 and to_add[1] < MAP_HEIGHT):
						#--Check potential space not already in list of checked spaces
						if not to_add in new_spaces:
							if not to_add in checked:
								#--Check potential space is open floor
								if map[to_add] == '.':
									#--Check potential space is goal
									if to_add == goal:
										return True
									else:
										new_spaces.append(to_add)
		#--After iterating through list, if no new spaces added, we've run out
		#--of potential spaces to check. Set cont = False to break loop.
		if len(new_spaces) == 0:
			cont = False
		#--New spaces added, so extend them into the list of checked spaces
		else:
			checked.extend(new_spaces)
	return False

def find_path():
	open_list.append([start, 0, 0, start])


def print_map():
	row = ''
	for x in xrange(MAP_WIDTH):
		for y in xrange(MAP_HEIGHT):
			if (x,y) == start:
				row += 'A'
			elif (x,y) == goal:
				row += 'Z'
			else:
				row += map[(x,y)]
			if y < MAP_HEIGHT - 1:
				row += ' '
		print(row)
		row = ''

def main():
	roll_map = True
	while roll_map:
		init_map()
		init_barriers()
		init_start()
		init_goal()

		if check_path_to_goal():
			print('Path to goal exists.')
			roll_map = False
		else:
			print('No path to goal found. Roll again.')
	find_path()
	print_map()

if __name__ == "__main__":
	main()


