class State:
	'''State represents a complete game board, and the moves to get to
	the current state of the game board.'''
	
	def __init__(self, board):
		self.board = board
		self.num_row = len(board)
		self.num_col = len(board[0])
		self.moves = []
	
	def possibleMoves(self):
		ret = []
		for i in range(self.num_row):
			for j in range(self.num_col):
				if self.board[i][j] != '0':
					continue
				if i >= 2 and self.board[i-1][j] != '0' and self.board[i-1][j] == self.board[i-2][j]:
					ret.append([[i, j], 3])
				if i < self.num_row - 2 and self.board[i+1][j] != '0' and self.board[i+1][j] == self.board[i+2][j]:
					ret.append([[i, j], 2])
				if j >= 2 and self.board[i][j-1] != '0' and self.board[i][j-1] == self.board[i][j-2]:
					ret.append([[i, j], 0])
				if j < self.num_col - 2 and self.board[i][j+1] != '0' and self.board[i][j+1] == self.board[i][j+2]:
					ret.append([[i, j], 1])
		return ret

	def isDone(self):
		for i in range(self.num_row):
			for j in range(self.num_col):
				if self.board[i][j] == 'c':
					while j < self.num_col:
						if self.board[i][j] != 'c' and self.board[i][j] != '0':
							return False
						j = j + 1
					return True
	
	def makeMove(self, move):
		self.moves.append(move)
		i = move[0][0]
		j = move[0][1]
		# move to right
		if move[1] == 0:
			self.board[i][j] = self.board[i][j-1]
			if self.board[i][j][0] == 't':
				self.board[i][j-3] = '0'
			else:
				self.board[i][j-2] = '0'
		# move to left
		elif move[1] == 1:
			self.board[i][j] = self.board[i][j+1]
			if self.board[i][j][0] == 't':
				self.board[i][j+3] = '0'
			else:
				self.board[i][j+2] = '0'
		# move to top
		elif move[1] == 2:
			self.board[i][j] = self.board[i+1][j]
			if self.board[i][j][0] == 't':
				self.board[i+3][j] = '0'
			else:
				self.board[i+2][j] = '0'
		# move to bottom
		else:
			self.board[i][j] = self.board[i-1][j]
			if self.board[i][j][0] == 't':
				self.board[i-3][j] = '0'
			else:
				self.board[i-2][j] = '0'
				
	def distanceToSol(self):
		count = 0
		for i in range(self.num_row):
			for j in range(self.num_col):
				if self.board[i][j] == 'c':
					while j < self.num_col:
						if self.board[i][j] == '0':
							count = count + 1
						elif self.board[i][j] != 'c':
							count = count + 2
						j = j + 1
					return count
			
	def __hash__(self):
		return hash(str(self.board))
	
	def __eq__(self, other):
		if not isinstance(other, type(self)):
			return NotImplemented
		return self.board == other.board

