from math import pow, sqrt, exp, cos, sin, pi
from configparser import ConfigParser
from ga import ga
from datetime import datetime


# Ackley  function
def fun1(x):
    return -20 * exp(-0.2 * sqrt(1 / len(x) * sum_square(x))) - exp(1 / len(x) * sum_cos(x)) + 20 + exp(1)


# Griewank function
def fun2(x):
    return sum_square_divide(x) - prod_cos(x) + 1


# Michalewicz function
def fun3(x):
    return -sum_sin(x)


def sum_square(x):
    result = 0
    for xi in x:
        result += pow(xi, 2)
    return result


def sum_cos(x):
    result = 0
    for xi in x:
        result += cos(2 * pi * xi)
    return result


def sum_square_divide(x):
    result = 0
    for xi in x:
        result += pow(xi, 2) / 4000
    return result


def prod_cos(x):
    product = 1
    for i in range(len(x)):
        product *= cos(x[i] / sqrt(i + 1))
    return product


def sum_sin(x):
    result = 0
    for i in range(len(x)):
        result += sin(x[i]) * pow(sin((i + 1) * pow(x[i], 2) / pi), 20)
    return result


def main():
    # Load user parameters from file
    config = ConfigParser()
    config.read('params.ini')

    # Choose function
    function_name = config['PARAMS']['function_name']
    if function_name == 'ackley':
        fun = fun1
    elif function_name == 'griewank':
        fun = fun2
    elif function_name == 'michalewicz':
        fun = fun3
    else:
        raise Exception('Function not supported!')

    # Do the algorithm
    now = datetime.now()
    x = ga(fun=fun,
           num_of_population=int(config['PARAMS']['num_of_population']),
           dimension=int(config['PARAMS']['dimension']),
           num_of_iterations=int(config['PARAMS']['num_of_iterations']),
           lower_bound=float(config['PARAMS']['lower_bound']),
           upper_bound=float(config['PARAMS']['upper_bound']),
           param_crossing=float(config['PARAMS']['param_crossing']),
           param_mutation=float(config['PARAMS']['param_mutation']),
           num_elitism=int(config['PARAMS']['elitism']))
    # Results
    print ('\n\nFunction results: \n')
    print ('x = {0}\nf(x) = {1}\n'.format(x, fun(x)))
    print ('Time: {0}'.format(datetime.now() - now))

if __name__ == '__main__':
    main()
