import random

class Map(object):
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.cells = {}
		for y in xrange(self.rows):
			for x in xrange(self.columns):
				self.cells[x,y] = '.'
		for i in xrange(int(.25 * self.rows * self.columns)):
			self.cells[self.get_random_free_cell()] = 'X'

	def get_random_free_cell(self):
		found = False
		while not found:
			loc = int(random.random() * self.columns), int(random.random() * self.rows)
			if self.cell_empty(loc):
				return loc

	def put_in_cell(self, loc, entity):
		self.cells[loc] = entity

	def cell_in_bounds(self, loc):
		'''Return True if cell is within map boundaries.'''
		if loc[0] >= 0 and loc[0] < self.columns:
			if loc[1] >= 0 and loc[1] < self.rows:
				return True
		return False

	def cell_empty(self, loc):
		'''Return True if cell contains empty floor.'''
		if self.cells[loc] == '.':
			return True
		return False

	def cell_passable(self, loc):
		'''Return True if cell is within map boundaries and also empty.'''
		if self.cell_in_bounds(loc):
			if self.cell_empty(self.cells[loc]):
				return True
		return False

	def print_map(self):
		for row in xrange(self.rows -1, -1, -1):
			row_string = ''
			for column in xrange(self.columns):
				row_string += self.cells[column, row] + ' '
			print(row_string)

	def get_path(self, start, end):
		# path = []
		openList = []

		return path

	def get_adjacents(self, loc):
		adjacents = []
		for x in xrange(-1, 2):
			for y in xrange(1, -2, -1):
				adj = loc[0] + x, loc[1] + y
				if adj != loc and self.cell_in_bounds(adj):
						adjacents.append(adj)
		return adjacents
