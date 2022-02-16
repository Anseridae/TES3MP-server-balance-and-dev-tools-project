from tkinter import *
from tkinter import ttk
import math


class calculations:
    distribution = []
    atLeastDistribution = []

    @staticmethod
    def exactDistributionCalc(chance, attempts):
        """return a binomial distribution to use later"""
        return [(math.comb(attempts, _) * (chance ** _) * ((1 - chance) ** (attempts - _)))
                for _ in range(attempts + 1)]

    def atLeastCalc(self):
        """find the chance of at least x successes in the distribution"""
        self.atLeastDistribution.clear()
        for i in range(1, len(self.distribution)):
            self.atLeastDistribution.append(1 - sum(self.distribution[0:i]))

    def printExact(self):
        """display the binomial distribution"""
        return [f"your chance of exactly {idx} successes is {val * 100}%"
                for idx, val in enumerate(self.distribution)]

    def printAtLeast(self):
        """display the chance of at least x successes in the distribution"""
        return [f"your chance of at least {idx + 1} successes is {val * 100}%"
                for idx, val in enumerate(self.atLeastDistribution)]

    def __init__(self):
        def myClick():
            try:
                self.distribution = \
                    self.exactDistributionCalc(float(successChanceBox.get()), int(attemptBox.get()))
                output1.config(text="\n".join(self.printExact()))
                self.atLeastCalc()
                output2.config(text="\n".join(self.printAtLeast()))
            except ValueError:
                output1.config(text="error")
                output2.config(text="")

        top = Toplevel()
        top.title("binomial probability tool")

        myLabel = Label(top, text="first enter in the chance of success for one attempt in decimal\n"
                        "E.g. instead of doing 70% you do 0.7 or just .70 if that's how you prefer to write it\n"
                        "then enter in the number of attempts you want to simulate\n")
        myLabel.pack()

        entryBar = ttk.Frame(top)
        entryBar.pack()

        entryLabel1 = Label(entryBar, text="enter chance for one success: ")
        entryLabel1.grid(row=0, column=0)

        successChanceBox = Entry(entryBar)
        successChanceBox.grid(row=0, column=1)

        entryLabel2 = Label(entryBar, text="enter number of attempts: ")
        entryLabel2.grid(row=1, column=0)

        attemptBox = Entry(entryBar)
        attemptBox.grid(row=1, column=1)

        calculateButton = Button(top, text="Calculate!", command=myClick)
        calculateButton.pack()

        outputGrid = ttk.Frame(top)
        outputGrid.pack()

        output1 = Label(outputGrid, text=" ", justify="left")
        output1.grid(row=0, column=0)

        output2 = Label(outputGrid, text=" ", justify="left")
        output2.grid(row=1, column=0)
