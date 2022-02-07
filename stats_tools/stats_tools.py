import math

distribution = []
atLeastDistribution = []


def exactDistributionCalc(chance, attempts):
    iterator = 0
    for _ in range(0, attempts + 1):
        binomialCoefficient = (math.comb(attempts, iterator) *
                               (chance ** iterator) * ((1 - chance) ** (attempts - iterator)))
        distribution.append(binomialCoefficient)
        iterator += 1
    return distribution


def atLeastCalc():
    iterator = 0
    accumulator = 0
    for i in distribution:
        accumulator += i
        atLeastDistribution.append(1 - accumulator)
        iterator += 1
    atLeastDistribution.pop()
    return atLeastDistribution


def printExact():
    iterator = 0
    for i in distribution:
        print("your chance of exactly " + str(iterator) + " successes is "
              + str(i * 100) + "%")
        iterator += 1


def printAtLeast():
    iterator = 1
    for i in atLeastDistribution:
        print("your chance of at least " + str(iterator) + " successes is "
              + str(i * 100) + "%")
        iterator += 1
