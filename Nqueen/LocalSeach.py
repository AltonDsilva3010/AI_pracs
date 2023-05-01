import random

# Define the N-Queens problem
def n_queens(n):
    board = [-1] * n
    for i in range(n):
        board[i] = random.randint(0, n-1)
    return board

# Define the cost function
def cost(board):
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(i-j) == abs(board[i]-board[j]):
                attacks += 1
    return attacks

# Define the hill climbing algorithm
def hill_climbing(n):
    current = n_queens(n)
    current_cost = cost(current)
    while True:
        neighbors = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    neighbor = list(current)
                    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                    neighbors.append(neighbor)
        if not neighbors:
            break
        neighbor_costs = [cost(neighbor) for neighbor in neighbors]
        best_cost = min(neighbor_costs)
        if best_cost >= current_cost:
            break
        best_indices = [index for index in range(len(neighbor_costs)) if neighbor_costs[index] == best_cost]
        current = neighbors[random.choice(best_indices)]
        current_cost = best_cost
    return current, current_cost

# Test the algorithm
n = 4
solution, solution_cost = hill_climbing(n)
print(f"Solution: {solution}")
print(f"Solution cost: {solution_cost}")