from randomized_tsp.Ant import Ant
from randomized_tsp.utils import cost


def _ant_colony(num_of_cities, 
                distance_matrix, 
                num_of_ants,
                pheromone_evapouration):
    Q = 1
    pheromone_matrix = [[0.1] * num_of_cities
                         for _ in range(num_of_cities)]
    best_tour = None
    for _ in range(1000):
        ants = [Ant(0, num_of_cities)] * num_of_ants
        pheromone_changes = [[0] * num_of_cities
                             for _ in range(num_of_cities)]
        for ant in ants:
            ant.construct_tour(pheromone_matrix, distance_matrix)
            tour_cost = cost(num_of_cities, distance_matrix, ant.tour)
            if best_tour is None or tour_cost < cost(num_of_cities, distance_matrix, best_tour):
                best_tour = ant.tour

            for i in range(num_of_cities):
                pheromone_changes[ant.tour[i]][ant.tour[(i+1) % num_of_cities]] += Q / tour_cost

        for i in range(num_of_cities):
            pheromone_matrix[i] = [(1 - pheromone_evapouration) * old + change
                                   for old, change in zip(pheromone_matrix[i], pheromone_changes[i])]
    return best_tour, cost(num_of_cities, distance_matrix, best_tour)
