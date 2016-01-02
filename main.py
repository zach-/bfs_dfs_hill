from state import State
from copy import deepcopy
import sys	
import Queue
from hillclimb import HillClimb

def BFS(start):
	q = Queue.Queue()
	q.put(start)
	visited = set()
	visited.add(start)
	
	while not q.empty():
		cur = q.get()
		if cur.isDone():
			return cur.moves
		possibleMoves = cur.possibleMoves()
		for move in possibleMoves:
			newState = deepcopy(cur)
			newState.makeMove(move)
			if newState not in visited:
				q.put(newState)
				visited.add(newState)

def DFS(start):
	q = Queue.LifoQueue()
	q.put(start)
	visited = set()
	visited.add(start)
	
	while not q.empty():
		cur = q.get()
		if cur.isDone():
			return cur.moves
		possibleMoves = cur.possibleMoves()
		for move in possibleMoves:
			newState = deepcopy(cur)
			newState.makeMove(move)
			if newState not in visited:
				q.put(newState)
				visited.add(newState)


def recursive_DFS_helper(start, depth):
	if depth == 0 and start.isDone():
		return []
	q = Queue.LifoQueue()
	q.put(start)
	visited = set()
	visited.add(start)
	print "depth is ", depth	
	while not q.empty():
		cur = q.get()
		if cur.isDone():
			return cur.moves
		possibleMoves = cur.possibleMoves()
		for move in possibleMoves:
			newState = deepcopy(cur)
			newState.makeMove(move)
			if len(newState.moves) <= depth and newState not in visited:
				q.put(newState)
				visited.add(newState)

def recursive_DFS(start):
	depth = 0
	while True:
		ret = recursive_DFS_helper(start, depth)
		if ret is not None:
			return ret
		depth = depth + 1

def readBoard(filename):
	f = open(filename, "r")
	ret = []
	for line in f:
		ret.append(line.strip().split(" "))
	return ret
		
# test case in the spec
#board = [['0', '0', '0', 't1', '0', '0'], ['0', '0', '0', 't1', '0', '0'], ['0', 'c', 'c', 't1', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0']]

# test case 1
#board = [['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', 'c', 'c', '0']]

# test case 2
#board = [['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', 'c', 'c', 't1'], ['0', '0', '0', '0', '0', 't1'], ['0', '0', '0', '0', '0', 't1'], ['0', '0', '0', '0', '0', '0']]

# test case 3
#board = [['0', '0', '0', 'c1', 'c1', 't1'], ['0', '0', '0', '0', 'c2', 't1'], ['0', '0', 'c', 'c', 'c2', 't1'], ['0', '0', '0', 't2', 't2', 't2'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', 't3', 't3', 't3']]

# test case 4
#board = [['c1', 'c1', '0', '0', '0', 't2'], ['t3', '0', '0', 't4', '0', 't2'], ['t3', 'c', 'c', 't4', '0', 't2'], ['t3', '0', '0', 't4', '0', '0'], ['c5', '0', '0', '0', 'c6', 'c6'], ['c5', '0', 't7', 't7', 't7', '0']]

if len(sys.argv) != 2:
	print "Please use python main.py <board_filename> to run the program"
	exit(0)
board = readBoard(sys.argv[1])
start = State(board)
print("using breadth first search...")
print(BFS(start))
print("using depth first search...")
print(DFS(start))
print("using iterative deepening search...")
print(recursive_DFS(start))
print("using hill climbing search...")
print(HillClimb(start))

