from tkinter import *
from tkinter import ttk


class hitChanceStat:

    @staticmethod
    def hitChanceCalc(weaponSkill, attackerAgility, attackerLuck, attackerFatigueTerm, attackerAttackBonus,
                      attackerBlind, defenderAgility, defenderLuck, defenderFatigueTerm, defenderSanctuary,
                      fCombatInvisoMult, defenderChameleon, defenderInvisibility):

        attackTerm = (weaponSkill + 0.2 * attackerAgility + 0.1 * attackerLuck) * attackerFatigueTerm
        attackTerm += attackerAttackBonus - attackerBlind

        defenseTerm = (0.2 * defenderAgility + 0.1 * defenderLuck) * defenderFatigueTerm
        defenseTerm += min(100, defenderSanctuary)

        defenseTerm += min(100.0, fCombatInvisoMult * defenderChameleon)
        defenseTerm += min(100.0, fCombatInvisoMult * defenderInvisibility)

        return round(attackTerm - defenseTerm)

    def __init__(self):
        def myClick():
            try:
                output1.config(text="hit chance = " + (str(self.hitChanceCalc(int(weaponSkillBox.get()),
                                                                              int(attackerAgilityBox.get()),
                                                                              int(attackerLuckBox.get()),
                                                                              float(attackerFatigueTermBox.get()),
                                                                              int(attackerAttackBonusBox.get()),
                                                                              int(attackerBlindBox.get()),
                                                                              int(defenderAgilityBox.get()),
                                                                              int(defenderLuckBox.get()),
                                                                              float(defenderFatigueTermBox.get()),
                                                                              int(defenderSanctuaryBox.get()),
                                                                              float(fCombatInvisoMultBox.get()),
                                                                              int(defenderChameleonBox.get()),
                                                                              int(defenderInvisibilityBox.get()))))
                                    + "%")
            except ValueError:
                output1.config(text="error")

        top = Toplevel()
        top.title("hit chance tool")

        myLabel = Label(top,
                        text="fCombatInvisoMult is a GMST with a default value of 0.2")
        myLabel.pack()

        entryBar = ttk.Frame(top)
        entryBar.pack()

        label1 = Label(entryBar, text="attacker stats: ")
        label1.grid(row=0, column=0, columnspan=2)

        entryLabel1 = Label(entryBar, text="weapon skill: ")
        entryLabel1.grid(row=1, column=0)

        weaponSkillBox = Entry(entryBar)
        weaponSkillBox.grid(row=1, column=1)

        entryLabel2 = Label(entryBar, text="attacker agility: ")
        entryLabel2.grid(row=2, column=0)

        attackerAgilityBox = Entry(entryBar)
        attackerAgilityBox.grid(row=2, column=1)

        entryLabel3 = Label(entryBar, text="attacker luck: ")
        entryLabel3.grid(row=3, column=0)

        attackerLuckBox = Entry(entryBar)
        attackerLuckBox.grid(row=3, column=1)

        entryLabel4 = Label(entryBar, text="attacker fatigueTerm: ")
        entryLabel4.grid(row=4, column=0)

        attackerFatigueTermBox = Entry(entryBar)
        attackerFatigueTermBox.grid(row=4, column=1)

        entryLabel5 = Label(entryBar, text="attacker attack bonus: ")
        entryLabel5.grid(row=5, column=0)

        attackerAttackBonusBox = Entry(entryBar)
        attackerAttackBonusBox.grid(row=5, column=1)

        entryLabel6 = Label(entryBar, text="attacker blind: ")
        entryLabel6.grid(row=6, column=0)

        attackerBlindBox = Entry(entryBar)
        attackerBlindBox.grid(row=6, column=1)

        label7 = Label(entryBar, text="defender stats: ")
        label7.grid(row=7, column=0, columnspan=2)

        entryLabel8 = Label(entryBar, text="defender agility: ")
        entryLabel8.grid(row=8, column=0)

        defenderAgilityBox = Entry(entryBar)
        defenderAgilityBox.grid(row=8, column=1)

        entryLabel9 = Label(entryBar, text="defender luck: ")
        entryLabel9.grid(row=9, column=0)

        defenderLuckBox = Entry(entryBar)
        defenderLuckBox.grid(row=9, column=1)

        entryLabel10 = Label(entryBar, text="defender fatigueTerm: ")
        entryLabel10.grid(row=10, column=0)

        defenderFatigueTermBox = Entry(entryBar)
        defenderFatigueTermBox.grid(row=10, column=1)

        entryLabel11 = Label(entryBar, text="defender sanctuary: ")
        entryLabel11.grid(row=11, column=0)

        defenderSanctuaryBox = Entry(entryBar)
        defenderSanctuaryBox.grid(row=11, column=1)

        entryLabel12 = Label(entryBar, text="fCombatInvisoMult: ")
        entryLabel12.grid(row=12, column=0)

        fCombatInvisoMultBox = Entry(entryBar)
        fCombatInvisoMultBox.insert(0, "0.2")
        fCombatInvisoMultBox.grid(row=12, column=1)

        entryLabel13 = Label(entryBar, text="defender chameleon: ")
        entryLabel13.grid(row=13, column=0)

        defenderChameleonBox = Entry(entryBar)
        defenderChameleonBox.grid(row=13, column=1)

        entryLabel14 = Label(entryBar, text="defender invisibility: ")
        entryLabel14.grid(row=14, column=0)

        defenderInvisibilityBox = Entry(entryBar)
        defenderInvisibilityBox.grid(row=14, column=1)

        calculateButton = Button(top, text="Calculate!", command=myClick)
        calculateButton.pack()

        outputGrid = ttk.Frame(top)
        outputGrid.pack()

        output1 = Label(outputGrid, text=" ", justify="left")
        output1.grid(row=0, column=0)
