import random
from randomized_tsp.utils import cost, random_neighbour, random_tour


def init_population(population_size, num_of_cities):
    """
    Initializes the population
    """
    population = set()
    while len(population) != population_size:
        population.add(tuple(random_tour(num_of_cities)))
    return [list(tour) for tour in population]


def calculate_fitness(population, num_of_cities, distance_matrix):
    """
    Return a fitness list for the population
    Fitness is just 1 / cost(tour)
    """
    fitness = [1 / cost(num_of_cities, distance_matrix, tour) 
               for tour in population]
    sum_fitness = sum(fitness)
    return [f / sum_fitness for f in fitness]


def order_crossover(num_of_cities, parent1, parent2):
    """
    Implements order crossover operator
    """
    start = random.randint(0, num_of_cities - 2)
    end = random.randint(start, num_of_cities - 1)
    child1 = parent1[start:end]
    child2 = parent2[start:end]
    for city in parent1:
        if city not in child2:
            child2.append(city)
    for city in parent2:
        if city not in child1:
            child1.append(city)
    return [child1, child2]


def cycle_crossover(num_of_cities, parent1, parent2):
    """
    Implements cycle crossover operator
    """
    child1 = [-1] * num_of_cities
    child2 = child1.copy()

    i = 0
    while child1[i] == -1:
        child1[i] = parent1[i]
        i = parent1.index(parent2[i])

    i = 0
    while child2[i] == -1:
        child2[i] = parent2[i]
        i = parent2.index(parent1[i])

    for i in range(num_of_cities):
        if child1[i] == -1:
            child1[i] = parent2[i]

        if child2[i] == -1:
            child2[i] = parent1[i]
    return [child1, child2]        


def mutate(num_of_cities, child):
    """
    Given a child will will give a mutation
    Mutation is just random exchange any two cities
    """
    return random_neighbour(num_of_cities, child)


def _genetic_algorithm(num_of_cities,
                       distance_matrix,
                       population_size,
                       mutation_prob,
                       crossover):
    """
    Implements the genetic algorithm for TSP
    Returns the best tour found and cost of that tour
    """
    crossover_func = order_crossover
    if crossover == 'cycle':
        crossover_func = cycle_crossover

    population = init_population(population_size, num_of_cities)

    num_of_epochs = num_of_cities * 2
    # In my experience a good value for `num_of_epochs` is directly
    # proportional to `num_of_cities`.
    # You can also experiment with different terminating condition
    for _ in range(num_of_epochs):
        # selection
        fitness = calculate_fitness(population, num_of_cities, distance_matrix)
        selected = random.choices(population, fitness, k=population_size)
        random.shuffle(selected)

        # offsprings
        offsprings = []
        for i in range(population_size // 2):
            children = crossover_func(num_of_cities, selected[i], selected[i + population_size // 2])
            offsprings.extend(children)

        # mutation
        for index in range(population_size):
            if random.uniform(0, 1) < mutation_prob:
                offsprings[index] = mutate(num_of_cities, offsprings[index])

        # replacement
        population.extend(offsprings)
        fitness = calculate_fitness(population, num_of_cities, distance_matrix)
        population = [tour for _, tour in sorted(zip(fitness, population), reverse=True)]
        population = population[:population_size]
    return population[0], cost(num_of_cities, distance_matrix, population[0])
