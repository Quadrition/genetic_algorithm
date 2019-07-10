from random import uniform



def generate_init_population(dim_population, dim_x, lb, ub):
    '''
    Generating initial population (random numbers)

    Attributes
    ----------
    dim_population : int
        number of units
    dim_x : int
        dimension of each unit
    lb : int
        lower bound for each coordinate
    up : int
        upper bound for each coordinate

    Returns
    -------
    population
        a list of radnom generated units
    '''
    population = []
    for j in range(dim_population):
        x = []
        for i in range(dim_x):
            x.append(uniform(lb, ub))
        population.append(x)
    return population


def calculate_chances(length):
    '''
    Generating a ranking list that is used in selecting units.
    Each element in ranking represent a procent chance of selecting unit.

    Attributes
    ----------
    length : int
        number of units

    Returns
    -------
    ranks
        a list of ranked units
    '''
    ranks = []
    rangs = range(length, 0, -1)
    s = sum(rangs)
    for i in rangs:
        ranks.append(i / s)
    return ranks


def roulette(psel):
    '''
    Takes a random unit based on ranks.
    The better rank - the bigger chance for unit to be selected

    Attributes
    ----------
    psel : list
        list of chances

    Returns
    -------
    unit
        a random selected unit
    '''
    number = uniform(0, 1)
    foo = 0
    for i in range(len(psel)):
        foo += psel[i]
        if number <= foo:
            return i
    return len(psel) - 1


def heuristic(x1, x2):
    '''
    Crosses two units
    Picks a random number from 0 to 1 and
    do the crossing based on that parameter

    Attributes
    ----------
    x1 : list
        first unit to be crossed
    x2 : list
        second unit to be crossed

    Returns
    -------
    x
        a crossed unit
    '''
    r = uniform(0, 1)
    x = []
    for i in range(len(x1)):
        x.append(r * (x1[i] - x2[i]) + x2[i])
    return x


def mutation(x, pm):
    '''
    Mutates a unit
    The chances of mutation depends on parameter
    passed by user.

    Attributes
    ----------
    x : list
        a unit that needs to be mutated
    pm : int
        chances for coordinate to be mutated
    '''
    for i in range(len(x)):
        r = uniform(0, 1)
        if r < pm:
            sign = int((10**5) * r) % 2
            x[i] += (-1) ** sign * uniform(0.4, 0.7)


def ga(fun, num_of_population, num_of_iterations, dimension, lower_bound, upper_bound, param_crossing, param_mutation, num_elitism):
    '''
    do the genetic algorithm

    Attributes
    ----------
    user passed parameters

    '''
    # Generate initialize population (random)
    generation = generate_init_population(num_of_population, dimension, lower_bound, upper_bound)
    # Iterator
    k = 0
    psel1 = calculate_chances(num_of_population)
    while k < num_of_iterations:
        # Sort best of them
        generation.sort(key=fun)
        if len(generation) != num_of_population:
            generation = generation[0:num_of_population]
        new_generation = []

        # Elitism
        for i in range(num_elitism):
            new_generation.append(generation[i][:])

        while len(new_generation) < num_of_population:
            # warning - optimization required
            index1 = roulette(psel1)
            # psell = psel(dim_population, q, r)
            # print ("New: " + str(len(new_generation)) + "Old: " + str(dim_population))
            # print (len(new_generation))
            index2 = roulette(psel1)
            while index1 == index2:
                index2 = roulette(psel1)
            r = uniform(0, 1)
            x1 = None
            x2 = None
            if r < param_crossing:
                # ukrstanje
                x1 = heuristic(generation[index1], generation[index2])
                x2 = heuristic(generation[index1], generation[index2])
            else:
                x1 = generation[index1][:]
                x2 = generation[index2][:]
            mutation(x1, param_mutation)
            mutation(x2, param_mutation)
            u1 = False
            u2 = False
            for i in range(len(x1)):
                if not (lower_bound <= x1[i] <= upper_bound):
                    u1 = True
                if not (lower_bound <= x2[i] <= upper_bound):
                    u2 = True
            if not u1:
                new_generation.append(x1)
            if not u2:
                new_generation.append(x2)
        generation = new_generation
        k = k + 1
        # print ('Best result in {0}. generation'.format(k))
        # print('x = {}'.format(generation[0]))
        # print ('f(x) = {}\n'.format(fun(generation[0])))
    generation.sort(key=fun)
    return generation[0]
