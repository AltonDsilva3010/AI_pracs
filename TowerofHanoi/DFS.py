class State:
    def __init__(self, pegs, moves):
        self.pegs = pegs
        self.moves = moves

    def next_states(self):
        next_states = []
        for i in range(3):
            for j in range(3):
                if i != j and len(self.pegs[i]) > 0 and (len(self.pegs[j]) == 0 or self.pegs[i][-1] < self.pegs[j][-1]):
                    new_pegs = [self.pegs[0][:], self.pegs[1][:], self.pegs[2][:]]
                    new_pegs[j].append(new_pegs[i].pop())
                    new_moves = self.moves[:]
                    new_moves.append((i, j))
                    next_states.append(State(new_pegs, new_moves))
        return next_states


def bfs(start, goal):
    visited = set()
    queue = [start]

    while queue:
        current = queue.pop()
        if current.pegs == goal:
            return current.moves
        if str(current.pegs) in visited:
            continue
        visited.add(str(current.pegs))
        queue.extend(current.next_states())

    return None


start_pegs = [[3, 2, 1], [], []]
goal_pegs = [[], [], [3, 2, 1]]
start_state = State(start_pegs, [])
moves = bfs(start_state, goal_pegs)
if moves:
    print(f"Solution found in {len(moves)} moves: {moves}")
else:
    print("No solution found.")
