from stats_tools_module import stats_tools


def main():
    print("welcome to the stats tool thingy I made in about an hour of googling stuff :P\n"
          "\n"
          "first enter in the chance of success for one attempt in decimal\n"
          "E.g. instead of doing 70% you do 0.7 or just .70 if that's how you prefer to write it\n"
          "then enter in the number of attempts you want to simulate\n")

    stats_tools.distribution = \
        stats_tools.exactDistributionCalc(float(input("plz enter the chance for one success: ")),
                                          int(input("plz enter the number of attempts you wanna simulate: ")))
    print("\nhere is the binomial distribution")
    stats_tools.printExact()
    print("\n"
          "here's another stats thingy")
    stats_tools.atLeastCalc()
    stats_tools.printAtLeast()
    input("\n"
          "press enter to exit")


if __name__ == '__main__':
    main()
