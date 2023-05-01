class State:
    def __init__(self,pegs,moves):
        self.pegs = pegs
        self.moves = moves

    def getnextstates(self):
        next_states = []
        for i in range(3):
            for j in range(3):
                if i != j and len(self.pegs[i]) > 0 and (len(self.pegs[j]) == 0 or self.pegs[i][-1] < self.pegs[j][-1]):
                    newpegs = [self.pegs[0][:],self.pegs[1][:],self.pegs[2][:]]
                    newpegs[j].append(newpegs[i].pop()) #add pegs from i to j
                    new_moves = self.moves[:]
                    new_moves.append((i,j))
                    next_states.append(State(newpegs,new_moves))


        return next_states


def bfs(start_state,goal):
    visited = set()
    queue = [start_state]
    while queue:
        current = queue.pop(0)
        if current.pegs == goal:
            return current.moves
        if str(current.pegs) in visited:
            continue
        visited.add(str(current.pegs))
        queue.extend(current.getnextstates())

    return None

start_pegs = [[3,2,1],[],[]] 
goal_pegs = [[],[],[3,2,1]] 
start_state = State(start_pegs,[])
moves = bfs(start_state,goal_pegs)
if moves:
    print(f"Solution found in {len(moves)} moves: {moves}")
else:
    print("No solution found.")