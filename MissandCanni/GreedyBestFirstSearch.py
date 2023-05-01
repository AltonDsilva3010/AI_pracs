from queue import PriorityQueue

class State:
    def __init__(self, m_left, c_left, m_right, c_right, boat_side):
        self.m_left = m_left
        self.c_left = c_left
        self.m_right = m_right
        self.c_right = c_right
        self.boat_side = boat_side
        self.parent = None

    def is_valid(self):
        if self.m_left < 0 or self.c_left < 0 or self.m_right < 0 or self.c_right < 0:
            return False
        if self.m_left != 0 and self.m_left < self.c_left:
            return False
        if self.m_right != 0 and self.m_right < self.c_right:
            return False
        return True

    def is_goal(self):
        return self.m_left == 0 and self.c_left == 0
    
    def __lt__(self, other):
        return (self.heuristic()) < (other.heuristic())

    def __eq__(self, other):
        return (self.m_left, self.c_left, self.m_right, self.c_right, self.boat_side) == (other.m_left, other.c_left, other.m_right, other.c_right, other.boat_side)

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.m_right, self.c_right, self.boat_side))
    
    def heuristic(self):
        return self.m_left + self.c_left

def successors(state):
    children = []
    if state.boat_side == 'left':
        for m in range(3):
            for c in range(3):
                if m + c >= 1 and m + c <= 2:
                    new_state = State(state.m_left - m, state.c_left - c, state.m_right + m, state.c_right + c, 'right')
                    if new_state.is_valid():
                        new_state.parent = state
                        children.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if m + c >= 1 and m + c <= 2:
                    new_state = State(state.m_left + m, state.c_left + c, state.m_right - m, state.c_right - c, 'left')
                    if new_state.is_valid():
                        new_state.parent = state
                        children.append(new_state)
    return children

def greedy_best_first_search(start_state):
    visited, queue = set(), PriorityQueue()
    queue.put((start_state.heuristic(), start_state))
    while queue:
        state = queue.get()[1]
        if state.is_goal():
            path = []
            while state.parent:
                path.append(state)
                state = state.parent
            path.append(state)
            path.reverse()
            return path
        visited.add((state.m_left, state.c_left, state.m_right, state.c_right, state.boat_side))
        for child in successors(state):
            if (child.m_left, child.c_left, child.m_right, child.c_right, child.boat_side) not in visited:
                queue.put((child.heuristic(), child))
                visited.add((child.m_left, child.c_left, child.m_right, child.c_right, child.boat_side))

start_state = State(3, 3, 0, 0, 'left')
path = greedy_best_first_search(start_state)
for state in path:
    print(f"State({state.m_left}, {state.c_left}, {state.m_right}, {state.c_right}, '{state.boat_side}')")
