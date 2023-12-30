import pygame
from constants import colors

class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = colors.WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == colors.RED

	def is_open(self):
		return self.color == colors.GREEN

	def is_barrier(self):
		return self.color == colors.BLACK

	def is_start(self):
		return self.color == colors.ORANGE

	def is_end(self):
		return self.color == colors.TURQUOISE

	def reset(self):
		self.color = colors.WHITE

	def make_start(self):
		self.color = colors.ORANGE

	def make_closed(self):
		self.color = colors.RED

	def make_open(self):
		self.color = colors.GREEN

	def make_barrier(self):
		self.color = colors.BLACK

	def make_end(self):
		self.color = colors.TURQUOISE

	def make_path(self):
		self.color = colors.PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, colors.GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, colors.GREY, (j * gap, 0), (j * gap, width))
			
def draw(win, grid, rows, width):
	win.fill(colors.WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col