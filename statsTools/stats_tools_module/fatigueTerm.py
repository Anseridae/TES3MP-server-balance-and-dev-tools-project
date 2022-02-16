from tkinter import *
from tkinter import ttk


class fatigueStat:

    @staticmethod
    def normalizedFatigueCalc(fFatigueBase, fFatigueMult, maxFatigue, currentFatigue):
        if maxFatigue == 0:
            normalizedFatigue = 1
        else:
            normalizedFatigue = max(0.0, currentFatigue / maxFatigue)
        # it is possible for normalizedFatigue to go over 1.0 when fatigue is fortified, it is not capped from above.
        return fFatigueBase - fFatigueMult * (1 - normalizedFatigue)
        # where normalizedFatigue is a function of actor fatigue. empty fatigue bar -> 0.0, full fatigue bar -> 1.0

    def __init__(self):
        def myClick():
            try:
                output1.config(text="fatigue term = " + (str(self.normalizedFatigueCalc(float(fFatigueBaseBox.get()),
                                                                                        float(fFatigueMultBox.get()),
                                                                                        int(maxFatigueBox.get()),
                                                                                        int(currentFatigueBox.get())))))
            except ValueError:
                output1.config(text="error")

        top = Toplevel()
        top.title("fatigueTerm tool")

        myLabel = Label(top,
                        text="fFatigueBase and fFatigueMult are GMSTs with default vales of 1.25 and 0.5 respectively")
        myLabel.pack()

        entryBar = ttk.Frame(top)
        entryBar.pack()

        entryLabel1 = Label(entryBar, text="fFatigueBase: ")
        entryLabel1.grid(row=0, column=0)

        fFatigueBaseBox = Entry(entryBar)
        fFatigueBaseBox.insert(0, "1.25")
        fFatigueBaseBox.grid(row=0, column=1)

        entryLabel2 = Label(entryBar, text="fFatigueMult: ")
        entryLabel2.grid(row=1, column=0)

        fFatigueMultBox = Entry(entryBar)
        fFatigueMultBox.insert(0, "0.5")
        fFatigueMultBox.grid(row=1, column=1)

        entryLabel3 = Label(entryBar, text="maxFatigue: ")
        entryLabel3.grid(row=2, column=0)

        maxFatigueBox = Entry(entryBar)
        maxFatigueBox.grid(row=2, column=1)

        entryLabel4 = Label(entryBar, text="currentFatigue: ")
        entryLabel4.grid(row=3, column=0)

        currentFatigueBox = Entry(entryBar)
        currentFatigueBox.grid(row=3, column=1)

        calculateButton = Button(top, text="Calculate!", command=myClick)
        calculateButton.pack()

        outputGrid = ttk.Frame(top)
        outputGrid.pack()

        output1 = Label(outputGrid, text=" ", justify="left")
        output1.grid(row=0, column=0)
