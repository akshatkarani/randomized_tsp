import random


def random_tour(num_of_cities):
    """
    Returns a random valid tour
    """
    tour = list(range(num_of_cities))
    random.shuffle(tour)
    return tour


def cost(num_of_cities, distance_matrix, tour):
    """
    Given `distance_matrix` and `num_of_cities`, calculates cost of a tour
    """
    cost = 0
    for i in range(num_of_cities):
        cost += distance_matrix[tour[i]][tour[(i+1) % num_of_cities]]
    return cost


def random_neighbour(num_of_cities, tour):
    """
    Two city exchange
    """
    new_tour = tour.copy()
    random_city = random.sample(range(num_of_cities), 2)
    new_tour[random_city[0]], new_tour[random_city[1]] = tour[random_city[1]], tour[random_city[0]]
    return new_tour
