from breezypythongui import EasyFrame
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
import random

class PFSCharacterCreator(EasyFrame):
    #Program for creating a Pathfinder Society (PFS) character
    charClass = ""

    def __init__(self):
        #Sets up the main window, labels, and buttons used in the program
        #Window setup for width, height, and title bar in Window
        EasyFrame.__init__(self, width = 800, height = 480, title = "PFS Character Creator")
        
        #Set Character Labels, PFS logo, boxes, and buttons
        imageLabel = self.addLabel(text = "", row=0, column=0, sticky="NW")
        self.image = PhotoImage(file="PFSLogo.gif")
        imageLabel["image"] = self.image
        self.addLabel(text = "Character Name: ", row = 1, column = 0, columnspan = 1, rowspan = 1,sticky = "NW")
        self.charName = self.addTextField(text = "Enter Character Name", row = 2, column = 0, width = 25, columnspan = 1, rowspan = 1, sticky = "NW")
        self.addButton(text = "Select Character Class", row = 3, column = 0, columnspan = 1, command = self.classSelect)
        self.charClass = self.addTextField(text = "Character Class", row = 4, column = 0, width = 25, columnspan = 1, rowspan = 1, sticky = "NW", state = "readonly")
        charClass = self.charClass
    
        #Ability Score labels
        self.addLabel(text = "Abilites", row = 2, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Strength", row = 3, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Dexterity", row = 4, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Constitution", row = 5, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Intelligence", row = 6, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Wisdom", row = 7, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Charisma", row = 8, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")

        #Ability Score addition and subtraction buttons
        self.addLabel(text = "Abilites + / -", row = 2, column = 4, columnspan = 2, rowspan = 1,sticky = "NSEW")
        self.addButton(text = " + ", row = 3, column = 4, columnspan = 1)
        self.addButton(text = " - ", row = 3, column = 5, columnspan = 1)
        self.addButton(text = " + ", row = 4, column = 4, columnspan = 1)
        self.addButton(text = " - ", row = 4, column = 5, columnspan = 1)
        self.addButton(text = " + ", row = 5, column = 4, columnspan = 1)
        self.addButton(text = " - ", row = 5, column = 5, columnspan = 1)
        self.addButton(text = " + ", row = 6, column = 4, columnspan = 1)
        self.addButton(text = " - ", row = 6, column = 5, columnspan = 1)
        self.addButton(text = " + ", row = 7, column = 4, columnspan = 1)
        self.addButton(text = " - ", row = 7, column = 5, columnspan = 1)
        self.addButton(text = " + ", row = 8, column = 4, columnspan = 1)
        self.addButton(text = " - ", row = 8, column = 5, columnspan = 1)

        #Ability Scores and Modifier integer fields
        self.addLabel(text = "Ability Scores", row = 2, column = 6, columnspan = 1, rowspan = 1,sticky = "NSW")
        self.outputFieldStrScore = self.addIntegerField(value = "10", row = 3, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldDexScore = self.addIntegerField(value = "10", row = 4, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldConScore = self.addIntegerField(value = "10", row = 5, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldIntScore = self.addIntegerField(value = "10", row = 6, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldWisScore = self.addIntegerField(value = "10", row = 7, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldChaScore = self.addIntegerField(value = "10", row = 8, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.addLabel(text = "Ability Modifier", row = 2, column = 7, columnspan = 1, rowspan = 1,sticky = "NSW")
        self.outputFieldStrMod = self.addIntegerField(value = "0", row = 3, column = 7, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldDexMod = self.addIntegerField(value = "0", row = 4, column = 7, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldConMod = self.addIntegerField(value = "0", row = 5, column = 7, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldIntMod = self.addIntegerField(value = "0", row = 6, column = 7, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldWisMod = self.addIntegerField(value = "0", row = 7, column = 7, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldChaMod = self.addIntegerField(value = "0", row = 8, column = 7, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        
        #Ability Points labels and buttons
        self.addLabel(text = "Point Total", row = 10, column = 4, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Point Spent", row = 9, column = 6, columnspan = 1, rowspan = 1,sticky = "NW")
        self.outputFieldPtsSpent = self.addIntegerField(value = "0", row = 10, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")        
        self.addLabel(text = "Point Left", row = 9, column = 7, columnspan = 1, rowspan = 1,sticky = "NW")
        self.outputFieldPtsLeft = self.addIntegerField(value = "20", row = 10, column = 7, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.addButton(text = "Reset Ability Scores", row = 11, column = 5, columnspan = 1, command = self.resetPoints)
        self.addButton(text = "Pick Abilities for me", row = 11, column = 6, columnspan = 1, command = self.autoPoints)

        #Die roller section - label and buttons to call each die roller
        self.addLabel(text = "Die Roller", row = 2, column = 9, columnspan = 1, rowspan = 1,sticky = "NSEW")
        self.addButton(text = "Roll a D20", row = 3, column = 9, columnspan = 1, command = self.rollD20)
        self.addButton(text = "Roll a D100", row = 4, column = 9, columnspan = 1, command = self.rollD100)
        self.addButton(text = "Roll a D12", row = 5, column = 9, columnspan = 1, command = self.rollD12)
        self.addButton(text = "Roll a D10", row = 6, column = 9, columnspan = 1, command = self.rollD10)
        self.addButton(text = "Roll a D8", row = 7, column = 9, columnspan = 1, command = self.rollD8)
        self.addButton(text = "Roll a D6", row = 8, column = 9, columnspan = 1, command = self.rollD6)
        self.addButton(text = "Roll a D4", row = 9, column = 9, columnspan = 1, command = self.rollD4)
        self.addButton(text = "Roll a D2", row = 10, column = 9, columnspan = 1, command = self.rollD2)
        self.outputFieldDieRoll = self.addIntegerField(value = "", row = 11, column = 9, state = "readonly", sticky="NSEW")

        #Buttons for resetting everything and for exiting program
        self.addButton(text = "Start Over / Reset", row = 0, column = 9, columnspan = 1, command = self.startOver)
        self.addButton(text = "Exit", row = 0, column = 10, columnspan = 1, command = self.exit)

    

    def classSelect(self):
        """Function for selecting your character Class and displaying character image"""
        #Prompts the user to select a Pathfinder Core Class from a listing in a new window
        #Text box is used as of now - I had some problems with Radio Button selection menus
        #Variable charClass is used for this function, and character image is based on charClass
        global charClass
        charClass = self.prompterBox(title = "Class", promptString = "Select your Class by typing in \nBarbarian \nBard \nCleric \nDruid \nFighter \nMonk \nPaladin \nRangerArcher \nRangerMelee \nRogue \nSorcerer \nWizard")
        self.charClass.setText(charClass)
        if charClass == "Barbarian":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Barbarian.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Bard":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Bard.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Cleric":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Cleric.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Druid":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Druid.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Fighter":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Fighter.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Monk":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Monk.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Paladin":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Paladin.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "RangerArcher":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="RangerArcher.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "RangerMelee":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="RangerMelee.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Rogue":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Rogue.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Sorcerer":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Sorcerer.gif")
            imageLabel["image"] = self.charImage
        elif charClass == "Wizard":
            imageLabel = self.addLabel(text = "", row=5, column=0, rowspan = 3, sticky="NW")
            self.charImage = PhotoImage(file="Wizard.gif")
            imageLabel["image"] = self.charImage
        return charClass

    def autoPoints(self):
        """Function for auto-selecting ability points based on Selected Class"""
        #Sets ability scores and modifiers based on optimal builds per rpgbot.net class guides
        #Uses the charClass variable for seeing which Class has been selected
        global charClass
        if charClass == "Barbarian":
            strScore = 17
            dexScore = 14
            conScore = 14
            intScore = 8
            wisScore = 13
            chaScore = 7
            strMod = 3
            dexMod = 2
            conMod = 2
            intMod = -1
            wisMod = 1
            chaMod = -2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Bard":
            strScore = 12
            dexScore = 14
            conScore = 14
            intScore = 11
            wisScore = 11
            chaScore = 15
            strMod = 1
            dexMod = 2
            conMod = 0
            intMod = 0
            wisMod = 0
            chaMod = 2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Cleric":
            strScore = 13
            dexScore = 10
            conScore = 12
            intScore = 8
            wisScore = 18
            chaScore = 10
            strMod = 2
            dexMod = 0
            conMod = 1
            intMod = -1
            wisMod = 4
            chaMod = 0        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Druid":
            strScore = 14
            dexScore = 14
            conScore = 14
            intScore = 9
            wisScore = 16
            chaScore = 7
            strMod = 2
            dexMod = 2
            conMod = 2
            intMod = -1
            wisMod = 3
            chaMod = -2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Fighter":
            strScore = 15
            dexScore = 17
            conScore = 14
            intScore = 7
            wisScore = 13
            chaScore = 8
            strMod = 2
            dexMod = 3
            conMod = 2
            intMod = -2
            wisMod = 2
            chaMod = -1        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Monk":
            strScore = 17
            dexScore = 13
            conScore = 14
            intScore = 8
            wisScore = 16
            chaScore = 7
            strMod = 3
            dexMod = 1
            conMod = 2
            intMod = -1
            wisMod = 3
            chaMod = -2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Paladin":
            strScore = 16
            dexScore = 12
            conScore = 14
            intScore = 10
            wisScore = 8
            chaScore = 14
            strMod = 3
            dexMod = 1
            conMod = 2
            intMod = 0
            wisMod = -1
            chaMod = -2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "RangerArcher":
            strScore = 12
            dexScore = 18
            conScore = 12
            intScore = 10
            wisScore = 13
            chaScore = 7
            strMod = 1
            dexMod = 4
            conMod = 1
            intMod = 0
            wisMod = 2
            chaMod = -2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "RangerMelee":
            strScore = 16
            dexScore = 14
            conScore = 14
            intScore = 11
            wisScore = 13
            chaScore = 7
            strMod = 3
            dexMod = 2
            conMod = 2
            intMod = 0
            wisMod = 2
            chaMod = -2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Rogue":
            strScore = 8
            dexScore = 17
            conScore = 14
            intScore = 12
            wisScore = 11
            chaScore = 12
            strMod = -1
            dexMod = 3
            conMod = 2
            intMod = 1
            wisMod = 2
            chaMod = 1        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Sorcerer":
            strScore = 7
            dexScore = 12
            conScore = 13
            intScore = 10
            wisScore = 12
            chaScore = 18
            strMod = -2
            dexMod = 1
            conMod = 1
            intMod = 0
            wisMod = 1
            chaMod = 4        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        elif charClass == "Wizard":
            strScore = 7
            dexScore = 14
            conScore = 14
            intScore = 18
            wisScore = 11
            chaScore = 7
            strMod = -2
            dexMod = 2
            conMod = 2
            intMod = 4
            wisMod = 1
            chaMod = -2        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(20)
            self.outputFieldPtsLeft.setNumber(0)
        else:
            strScore = 10
            dexScore = 10
            conScore = 10
            intScore = 10
            wisScore = 10
            chaScore = 10
            strMod = 0
            dexMod = 0
            conMod = 0
            intMod = 0
            wisMod = 0
            chaMod = 0        
            self.outputFieldStrScore.setNumber(strScore)
            self.outputFieldDexScore.setNumber(dexScore)
            self.outputFieldConScore.setNumber(conScore)
            self.outputFieldIntScore.setNumber(intScore)
            self.outputFieldWisScore.setNumber(wisScore)
            self.outputFieldChaScore.setNumber(chaScore)
            self.outputFieldStrMod.setNumber(strMod)
            self.outputFieldDexMod.setNumber(dexMod)
            self.outputFieldConMod.setNumber(conMod)
            self.outputFieldIntMod.setNumber(intMod)
            self.outputFieldWisMod.setNumber(wisMod)
            self.outputFieldChaMod.setNumber(chaMod)
            self.outputFieldPtsSpent.setNumber(0)
            self.outputFieldPtsLeft.setNumber(20)
            
    def resetPoints(self):
        """Function for resetting ability points"""
        #Resets ability scores, modifiers, and point pool back to defaults
        self.outputFieldStrScore.setNumber(10)
        self.outputFieldDexScore.setNumber(10)
        self.outputFieldConScore.setNumber(10)
        self.outputFieldIntScore.setNumber(10)
        self.outputFieldWisScore.setNumber(10)
        self.outputFieldChaScore.setNumber(10)
        self.outputFieldStrMod.setNumber(0)
        self.outputFieldDexMod.setNumber(0)
        self.outputFieldConMod.setNumber(0)
        self.outputFieldIntMod.setNumber(0)
        self.outputFieldWisMod.setNumber(0)
        self.outputFieldChaMod.setNumber(0)
        self.outputFieldPtsSpent.setNumber(0)
        self.outputFieldPtsLeft.setNumber(20)

    def startOver(self):
        """Function for starting over and returning all entries to defaults"""
        #Resets all fields back to defaults
        global charClass
        self.charName.setText("Enter Character Name")
        charClass = "Character Class"
        self.charClass.setText(charClass)
        imageLabel = self.addLabel(text = "", row=5, column=0, sticky="NW")
        self.charImage = None
        imageLabel["image"] = self.charImage
        self.outputFieldStrScore.setNumber(10)
        self.outputFieldDexScore.setNumber(10)
        self.outputFieldConScore.setNumber(10)
        self.outputFieldIntScore.setNumber(10)
        self.outputFieldWisScore.setNumber(10)
        self.outputFieldChaScore.setNumber(10)
        self.outputFieldStrMod.setNumber(0)
        self.outputFieldDexMod.setNumber(0)
        self.outputFieldConMod.setNumber(0)
        self.outputFieldIntMod.setNumber(0)
        self.outputFieldWisMod.setNumber(0)
        self.outputFieldChaMod.setNumber(0)
        self.outputFieldPtsSpent.setNumber(0)
        self.outputFieldPtsLeft.setNumber(20)
        self.outputFieldDieRoll.setNumber("")

    def exit(self):
        """Function for exiting the program"""
        exit()

    #Die Roller - ranges for each game die set - 20 sided (most common at top),
    #100 sided, 12 sided, 10 sided, 8, 6, 4, and 2 sided.
    def rollD20(self):
        """Function for rolling a 20 sided die"""
        d20 = random.randint(1,20)
        self.outputFieldDieRoll.setNumber(d20)
    def rollD100(self):
        """Function for rolling a 100 sided (percentile) die"""
        d100 = random.randint(1,100)
        self.outputFieldDieRoll.setNumber(d100)
    def rollD12(self):
        """Function for rolling a 12 sided die"""
        d12 = random.randint(1,12)
        self.outputFieldDieRoll.setNumber(d12)
    def rollD10(self):
        """Function for rolling a 10 sided die"""
        d10 = random.randint(1,10)
        self.outputFieldDieRoll.setNumber(d10)
    def rollD8(self):
        """Function for rolling a 8 sided die"""
        d8 = random.randint(1,8)
        self.outputFieldDieRoll.setNumber(d8)
    def rollD6(self):
        """Function for rolling a 6 sided die"""
        d6 = random.randint(1,6)
        self.outputFieldDieRoll.setNumber(d6)
    def rollD4(self):
        """Function for rolling a 4 sided die"""
        d4 = random.randint(1,4)
        self.outputFieldDieRoll.setNumber(d4)
    def rollD2(self):
        """Function for rolling a 2 sided die"""
        d2 = random.randint(1,2)
        self.outputFieldDieRoll.setNumber(d2) 
        
        
def main():
    """Main function of Pathfinder Character Creator"""
    #Instantiaties and pops up the window.
    PFSCharacterCreator().mainloop()

if __name__ == "__main__":
    main()



"""
Pathfinder Character Creator by Matthew Flispart
Last updated 10/10/2021

For documentation see Final Project Documentation.

New to Pathfinder? See the User Guide for how to build a character using this program.
"""
