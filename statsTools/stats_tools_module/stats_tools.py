import math

distribution = []
atLeastDistribution = []


def exactDistributionCalc(chance, attempts):
    """return a binomial distribution to use later"""
    return [(math.comb(attempts, _) * (chance ** _) * ((1 - chance) ** (attempts - _))) for _ in range(attempts + 1)]


def atLeastCalc():
    """find the chance of at least x successes in the distribution"""
    for i in range(1, len(distribution)):
        atLeastDistribution.append(1 - sum(distribution[0:i]))


def printExact():
    """display the binomial distribution"""
    return [print("your chance of exactly " + str(idx) + " successes is "
                  + str(val * 100) + "%") for idx, val in enumerate(distribution)]


def printAtLeast():
    """display the chance of at least x successes in the distribution"""
    return [print("your chance of at least " + str(idx + 1) + " successes is "
                  + str(val * 100) + "%") for idx, val in enumerate(atLeastDistribution)]
