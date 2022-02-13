from tkinter import *
from tkinter import ttk
from stats_tools_module import stats_tools


def main():

    def myClick():
        try:
            stats_tools.distribution = \
                stats_tools.exactDistributionCalc(float(successChanceBox.get()), int(attemptBox.get()))
            output1.config(text=stats_tools.printExact())
            stats_tools.atLeastCalc()
            output2.config(text=stats_tools.printAtLeast())
        except ValueError:
            output1.config(text="error")

    root = Tk()
    root.title("binomial probability tool")

    myLabel = Label(root, text="first enter in the chance of success for one attempt in decimal\n"
                               "E.g. instead of doing 70% you do 0.7 or just .70 if that's how you prefer to write it\n"
                               "then enter in the number of attempts you want to simulate\n")
    myLabel.pack()

    entryBar = ttk.Frame(root)
    entryBar.pack()

    entryLabel1 = Label(entryBar, text="enter chance for one success: ")
    entryLabel1.grid(row=0, column=0)

    successChanceBox = Entry(entryBar)
    successChanceBox.grid(row=0, column=1)

    entryLabel2 = Label(entryBar, text="enter number of attempts: ")
    entryLabel2.grid(row=1, column=0)

    attemptBox = Entry(entryBar)
    attemptBox.grid(row=1, column=1)

    myButton = Button(root, text="Calculate!", command=myClick)
    myButton.pack()

    outputGrid = ttk.Frame(root)
    outputGrid.pack()

    output1 = Label(outputGrid, text=" ")
    output1.grid(row=0, column=0)

    output2 = Label(outputGrid, text=" ")
    output2.grid(row=1, column=0)

    root.mainloop()


if __name__ == '__main__':
    main()
