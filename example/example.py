from randomized_tsp.tsp import tsp

distances = []
# `input_file` file contains 100 X 100 matrix
with open('input_file') as fp:
    for line in fp:
        distances.append([float(x) for x in line.strip().split(' ')])

t = tsp(distances)

# Run ant colony
tour1, cost1 = t.ant_colony()

# Run genetic algorithm
tour2, cost2 = t.genetic_algorithm()

# Run simulated annealing
tour3, cost3 = t.simulated_annealing()
