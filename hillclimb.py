from state import State
from copy import deepcopy
import Queue
def StateCompare(A, B):
	'''functions to compare two State '''
	return B.distanceToSol() - A.distanceToSol()

def HillClimb(start):
	q = Queue.LifoQueue()
	q.put(start)
	visited = set()
	visited.add(start)
	ret =[]
	first_sol = True
	
	while not q.empty():
		cur = q.get()
		if cur.isDone() and (first_sol or len(cur.moves) < len(ret)):
			ret = cur.moves
			first_sol = False
			#print "Found Local Maximum ", ret
		possibleMoves = cur.possibleMoves()
		newStatesList = []
		for move in possibleMoves:
			newState = deepcopy(cur)
			newState.makeMove(move)
			if (first_sol or len(newState.moves) < len(ret)) and newState not in visited:
				newStatesList.append(newState)
		newStatesList.sort(cmp = StateCompare)
		for state in newStatesList:
			q.put(state)
	
	return ret
