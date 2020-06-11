# randomized_tsp

A python3 package implementing randomized algorithms for [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
The implementations are based on [A first course in Artificial Intelligence: Deepak Khemani](https://www.mheducation.co.in/a-first-course-in-artificial-intelligence-9781259029981-india).

The algorithms implemented include:
- [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Ant Colony Optimization](https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms)

## Installation

You can install this using `pip`. Just run

``pip install randomized_tsp``

## Usage

If you have `n` cities in your problem then you need to define the distances between cities using a two dimensional `n X n` list.
`distances[i][j]` should give the distance between city i and city j.

```python
from randomized_tsp.tsp import tsp

# If you have 3 cities then you need to define this list 
# which gives the distances between two cities
distances = [[0, 4, 2], [4, 0, 3], [2, 3, 0]]

tsp_obj = tsp(distances)

# To run genetic algorithm
tour, cost = tsp_obj.genetic_algorithm()

# To run simulated annealing
tour, cost = tsp_obj.simulated_annealing()

# To run ant colony optimization
tour, cost = tsp_obj.ant_colony()
```

All the three algorithms return that best tour found and the cost of that tour. Tour is represented using path representation.


```python
def genetic_algorithm(self,
                      population_size=50,
                      mutation_prob=0.1,
                      crossover='order'):
        """
        :param population_size: Defines the size of the population used in the algorithm
        :param mutation_prob:   Probability that a offspring will mutate
        :param crossover:       Defines the crossover operator, currently two options are available
                                `order` and `cycle`.
        :return:                Returns the best tour found and the cost of that tour
                                A tour is represented using path representation
        """

def simulated_annealing(self):
        """
        :return: Returns the best tour found and the cost of that tour
                 A tour is represented using path representation
        """

def ant_colony(self,
               num_of_ants=20,
               pheromone_evapouration=0.2):
        """
        :param num_of_ants:            Number of ants in the colony
        :param pheromone_evapouration: Evapouration rate of the pheromone deposited by ants
        :return:                       Returns the best tour found and the cost of that tour
                                       A tour is represented using path representation
```


## Contributing

Many of these algorithms need improvements and optimizations. If you want to improve this project or fix a bug then all contributions are welcome. 

## Contact

If you find any bugs then contact me on [gitter](https://gitter.im/akshatkarani) and open a issue on this repository.
