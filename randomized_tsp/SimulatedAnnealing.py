from randomized_tsp.utils import cost, random_neighbour, random_tour
import math
import random


def sigmoid(x: float):
    return 1 / (1 + math.exp(x))


def cooling(temperature, time):
    """
    Defines different types of cooling functions
    `func_type` decides which function to use
    """
    return temperature / (time + 1)


def _simulated_annealing(num_of_cities, distance_matrix):
    tour = random_tour(num_of_cities)
    best_tour = tour
    temperature = num_of_cities ** 2
    num_of_epochs = 1000
    for time in range(num_of_epochs):
        for _ in range(1000):
            if temperature < 0.000009e-300:
                break
            neighbour = random_neighbour(num_of_cities, tour)
            delta_cost = cost(num_of_cities, distance_matrix, neighbour) - cost(num_of_cities, distance_matrix, tour)
            if random.uniform(0, 1) < sigmoid(delta_cost / temperature):
                tour = neighbour
                if cost(num_of_cities, distance_matrix, tour) < cost(num_of_cities, distance_matrix, best_tour):
                    best_tour = tour
                temperature = cooling(temperature, time)

    return best_tour
