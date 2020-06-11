import random


class Ant:

    def __init__(self, start_city, num_of_cities):
        """
        Initializes a new ant
        start_city is randomized for each ant
        """
        start_city = random.randint(0, num_of_cities - 1)
        self.to_visit = list(range(num_of_cities))
        self.to_visit.remove(start_city)
        self.tour = [start_city]

    def construct_tour(self, pheromone_matrix, distance_matrix):
        """
        Constructs a tour for a ant give the pheromone_matrix and distance_matrix
        """
        alpha = 100
        beta = 100
        current_city = self.tour[-1]
        while len(self.to_visit) != 0:
            prob_to_vist = []
            for next_city in self.to_visit:
                prob_to_vist.append((pheromone_matrix[current_city][next_city] ** alpha) +
                                    ((1 / distance_matrix[current_city][next_city]) ** beta))
            denominator_sum = sum(prob_to_vist)
            prob_to_vist = [prob / denominator_sum for prob in prob_to_vist]

            current_city = random.choices(self.to_visit, prob_to_vist, k=1)[0]
            self.tour.append(current_city)
            self.to_visit.remove(current_city)
