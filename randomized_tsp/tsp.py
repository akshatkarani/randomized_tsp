from randomized_tsp.SimulatedAnnealing import _simulated_annealing
from randomized_tsp.Genetic import _genetic_algorithm
from randomized_tsp.AntColony import _ant_colony
from randomized_tsp.utils import cost


class tsp:
    def __init__(self, distance_matrix):
        # distance_matrix[i][j] is the distance between city i and city j
        self.distance_matrix = distance_matrix
        self.num_of_cities = len(self.distance_matrix)

    
    def genetic_algorithm(self, population_size=50, mutation_prob=0.1, crossover='order'):
        tour = _genetic_algorithm(self.num_of_cities,
                                  self.distance_matrix,
                                  population_size=population_size,
                                  mutation_prob=mutation_prob,
                                  crossover=crossover)
        return tour, cost(self.num_of_cities, self.distance_matrix, tour)


    def simulated_annealing(self):
        tour = _simulated_annealing(self.num_of_cities,
                                    self.distance_matrix)
        return tour, cost(self.num_of_cities, self.distance_matrix, tour)


    def ant_colony(self):
        tour = _ant_colony(self.num_of_cities,
                           self.distance_matrix)
        return tour, cost(self.num_of_cities, self.distance_matrix, tour)
