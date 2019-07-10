# genetic_algorithm
In computer science and operations research, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.

In this project, we are going to use GA for finding a minimum in these functions:

1. Ackley https://www.sfu.ca/~ssurjano/ackley.html
2. Griewank https://www.sfu.ca/~ssurjano/griewank.html
3. Michalewicz https://www.sfu.ca/~ssurjano/michal.html

The application loads the parameters from the file parameters.ini, and use them for solving the algorithm. Different parameters may affects on different results and time of algorithm. 

These are the meaning of the parameters:

function_name - the name of the function that we are finding the minimum (michalewicz, ackley or griewank
num_of_population - number of population
dimension - dimenstion
num_of_iterations - number of iterations
lower_bound - lower bound of the function
upper_bound - upper bound of the function
param_crossing - chances of crossing to happen
param_mutation - chances of mutation to happen
elitism - number of elements in the populaton for elitism

The parameters for the best results found so far are in the directory "Best parameters".
