import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)

# Define cities and their coordinates
cities = np.array([
    [60, 200], [180, 200], [80, 180], [140, 180], [20, 160],
    [100, 160], [200, 160], [140, 140], [40, 120], [100, 120],
    [180, 100], [60, 80], [120, 80], [180, 60], [20, 40], [100, 40],
    [200, 40], [20, 20], [60, 20], [160, 20]
])

# Define genetic algorithm parameters
population_size = 100
num_generations = 1000
mutation_rate = 0.02

# Define fitness function
def calculate_fitness(individual, cities):
    total_distance = 0
    for i in range(len(individual) - 1):
        city_a = individual[i]
        city_b = individual[i+1]
        total_distance += np.linalg.norm(cities[city_a] - cities[city_b])
    return 1 / total_distance

# Define selection function
def selection(population):
    fitness_values = np.array([calculate_fitness(individual, cities) for individual in population])
    total_fitness = np.sum(fitness_values)
    probabilities = fitness_values / total_fitness
    selected_indices = np.random.choice(range(population_size), size=population_size, p=probabilities)
    return [population[index] for index in selected_indices]

# Define crossover function
def crossover(parent_a, parent_b):
    crossover_point = random.randint(1, len(parent_a) - 1)
    child_a = parent_a[:crossover_point] + [city for city in parent_b if city not in parent_a[:crossover_point]]
    child_b = parent_b[:crossover_point] + [city for city in parent_a if city not in parent_b[:crossover_point]]
    return child_a, child_b

# Define mutation function
def mutation(individual):
    if random.random() < mutation_rate:
        index_a = random.randint(0, len(individual) - 1)
        index_b = random.randint(0, len(individual) - 1)
        individual[index_a], individual[index_b] = individual[index_b], individual[index_a]
    return individual

# Generate initial population
population = [random.sample(range(len(cities)), len(cities)) for i in range(population_size)]

# Main genetic algorithm loop
for generation in range(num_generations):
    population = selection(population)
    offspring = []
    for i in range(int(population_size / 2)):
        parent_a = population[i]
        parent_b = population[population_size - i - 1]
        child_a, child_b = crossover(parent_a, parent_b)
        child_a = mutation(child_a)
        child_b = mutation(child_b)
        offspring.append(child_a)
        offspring.append(child_b)
    population = offspring

# Find best individual and print result
best_individual = max(population, key=lambda individual: calculate_fitness(individual, cities))
best_distance = 1 / calculate_fitness(best_individual, cities)
print("Best path found: {}".format(best_individual))
print("Distance of best path: {}".format(best_distance))