from collections import deque

def bfs_toh(num_disk):
    start_state = (tuple(range(num_disk,0,-1)),(),())
    goal_state = ((),(),tuple(range(num_disk,0,-1)))

    queue = deque([start_state])

    visited = set()

    parents = {}

    while queue:
        current_state = queue.popleft()

        if current_state == goal_state:
            path = []

            while current_state != start_state:
                path.append(current_state)
                current_state = parents[current_state]

            path.append(start_state)
            path.reverse()

            return path
        visited.add(current_state)
        valid_moves = get_valid_moves(current_state)
        for move in valid_moves:
            next_state = apply_move(current_state, move)
            if next_state not in visited:
                queue.append(next_state)
                parents[next_state] = current_state
        
    return None

def get_valid_moves(state):
    top_disks = [peg[-1] if peg else float('inf') for peg in state]
    valid_moves = []
    for i in range(len(state)):
        # Loop through each other peg
        for j in range(len(state)):
            if i != j:
                # If the top disk on peg i can be moved to peg j, add the move to the valid moves list
                if top_disks[i] < top_disks[j]:
                    valid_moves.append((i, j))
    return valid_moves

def apply_move(state, move):
    # Get the source and destination pegs from the move tuple
    src, dst = move

    # Get the lists of disks on the source and destination pegs from the state tuple
    src_list, dst_list = list(state[src]), list(state[dst])

    # Remove the top disk from the source peg and add it to the destination peg
    dst_list.append(src_list.pop())

    # Create a new state tuple with the updated peg lists
    new_state = list(state)
    new_state[src] = tuple(src_list)
    new_state[dst] = tuple(dst_list)

    # Return the new state tuple
    return tuple(new_state)

def main():
    num_disk = 3
    optimal_path = bfs_toh(num_disk)
    if optimal_path:
        print(f"Optimal path for {num_disk} :\n")
        for state in optimal_path:
            print_state(state)
            print()
    else:
        print("no solucion")

def print_state(state):
    for peg in state:
        print(peg)
    print("--------")

if __name__ == '__main__':
    main()