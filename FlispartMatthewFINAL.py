from breezypythongui import EasyFrame
from tkinter import PhotoImage
#from tkinter.font import font
import random

class PFSCharacterCreator(EasyFrame):
    #Program for creating a Pathfinder Society (PFS) character

    def __init__(self):
        #Sets up the window, label, and button
        #Window setup for width, height, and title bar in Window
        EasyFrame.__init__(self, width = 720, height = 480, title = "PFS Character Creator")
        

        #Set Character Labels, boxes, and buttons
        self.addLabel(text = "Pathfinder Society (PFS) Character Creator", row = 0, column = 0, columnspan = 1, rowspan = 1, sticky = "NW")
        self.addLabel(text = "Character Name: ", row = 1, column = 0, columnspan = 1, rowspan = 1,sticky = "NW")
        self.charName = self.addTextField(text = "Enter Character Name", row = 2, column = 0, width = 25, columnspan = 1, rowspan = 1, sticky = "NW")
        self.addButton(text = "Select Character Class", row = 3, column = 0, columnspan = 1, command = self.classSelect)
        self.charClass = self.addTextField(text = "Character Class", row = 4, column = 0, width = 25, columnspan = 1, rowspan = 1, sticky = "NW", state = "readonly")
        
    
        #Ability Score labels, Ability Score and Modifier integer fields
        self.addLabel(text = "Abilites", row = 2, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Strength", row = 3, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Dexterity", row = 4, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Constitution", row = 5, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Intelligence", row = 6, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Wisdom", row = 7, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Charisma", row = 8, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        
        self.addLabel(text = "Ability Scores", row = 2, column = 5, columnspan = 1, rowspan = 1,sticky = "NW")
        self.outputFieldStrScore = self.addIntegerField(value = "10", row = 3, column = 5, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldDexScore = self.addIntegerField(value = "10", row = 4, column = 5, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldConScore = self.addIntegerField(value = "10", row = 5, column = 5, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldIntScore = self.addIntegerField(value = "10", row = 6, column = 5, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldWisScore = self.addIntegerField(value = "10", row = 7, column = 5, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldChaScore = self.addIntegerField(value = "10", row = 8, column = 5, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")

        self.addLabel(text = "Ability Modifier", row = 2, column = 6, columnspan = 1, rowspan = 1,sticky = "NW")
        self.outputFieldStrMod = self.addIntegerField(value = "0", row = 3, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldDexMod = self.addIntegerField(value = "0", row = 4, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldConMod = self.addIntegerField(value = "0", row = 5, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldIntMod = self.addIntegerField(value = "0", row = 6, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldWisMod = self.addIntegerField(value = "0", row = 7, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.outputFieldChaMod = self.addIntegerField(value = "0", row = 8, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")


        #Ability Points labels and buttons
        self.addLabel(text = "Point Total", row = 10, column = 3, columnspan = 1, rowspan = 1,sticky = "NW")
        self.addLabel(text = "Point Spent", row = 9, column = 5, columnspan = 1, rowspan = 1,sticky = "NW")
        self.outputFieldPtsSpent = self.addIntegerField(value = "0", row = 10, column = 5, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")        
        self.addLabel(text = "Point Left", row = 9, column = 6, columnspan = 1, rowspan = 1,sticky = "NW")
        self.outputFieldPtsLeft = self.addIntegerField(value = "20", row = 10, column = 6, columnspan = 1, rowspan = 1,sticky = "NW", state = "readonly")
        self.addButton(text = "Reset Ability Scores", row = 11, column = 5, columnspan = 1, command = self.resetPoints)
        self.addButton(text = "Pick Abilities for me", row = 11, column = 6, columnspan = 1, command = self.autoPoints)

        #Die roller section - label and buttons to call each die roller
        self.addLabel(text = "Die Roller", row = 2, column = 8, columnspan = 1, rowspan = 1,sticky = "NSEW")
        self.addButton(text = "Roll a D20", row = 3, column = 8, columnspan = 1, command = self.rollD20)
        self.addButton(text = "Roll a D100", row = 4, column = 8, columnspan = 1, command = self.rollD100)
        self.addButton(text = "Roll a D12", row = 5, column = 8, columnspan = 1, command = self.rollD12)
        self.addButton(text = "Roll a D10", row = 6, column = 8, columnspan = 1, command = self.rollD10)
        self.addButton(text = "Roll a D8", row = 7, column = 8, columnspan = 1, command = self.rollD8)
        self.addButton(text = "Roll a D6", row = 8, column = 8, columnspan = 1, command = self.rollD6)
        self.addButton(text = "Roll a D4", row = 9, column = 8, columnspan = 1, command = self.rollD4)
        self.addButton(text = "Roll a D2", row = 10, column = 8, columnspan = 1, command = self.rollD2)
        self.outputFieldDieRoll = self.addIntegerField(value = "", row = 11, column = 8, state = "readonly")

        self.addButton(text = "Start Over / Reset", row = 1, column = 8, columnspan = 1, command = self.startOver)
        self.addButton(text = "Exit", row = 1, column = 9, columnspan = 1, command = self.exit)

             
        #Testing panels for future use
        #dataPanel = self.addPanel(row = 0, column = 1, background = "gray")
        #dataPanel.addLabel(text = "Label 1", row = 1, column = 1)
        #dataPanel.addTextField(text = "Text1", row = 1, column = 2)
        #dataPanel.addLabel(text = "Label 2", row = 2, column = 2)
        #dataPanel.addTextField(text = "Text1", row = 2, column = 2)

    #Testing a pop-up box for Class Selection with a Radio Button list
    #Current test is using promptString and returns charClass to Output Field
    def classSelect(self):
        """Function for selecting your character Class"""
        charClass = self.prompterBox(title = "Select your Character Class", promptString = "Class")
        self.charClass.setText(charClass)
        return charClass

    def autoPoints(self):
        """Function for auto-selecting ability points based on Class"""
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

    def resetPoints(self):
        """Function for resetting ability points"""
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
        self.charName.setText("Enter Character Name")
        self.charClass.setText("")
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
    #Instantiaties and pops up the window.
    PFSCharacterCreator().mainloop()

if __name__ == "__main__":
    main()



"""
Code from previous GUI project work to keep in mind


        #self.addLabel(text = "The converted temperature is: ", row = 8, column = 0)
        #self.outputField = self.addFloatField(value = 0.0,
                                               row = 9,
                                               column = 1,
                                               width = 10,
                                               precision = 2,
                                               state = "readonly")
        
        #Label for output of converted temperature and screen placement
        
      #  self.addButton(text = "Convert Celsius to Fahrenheit", row = 2, column = 0,
                   #    columnspan = 2,
                   #    command = self.convertCtoF)
        #Button for running the conversion and displaying C to F in outputField

     #   self.addButton(text = "Convert Fahrenheit to Celsius", row = 3, column = 0,
                  #     columnspan = 2,
                #    command = self.convertFtoC)
        #Button for running the conversion and displaying F to C in outputField

  #  def convertCtoF(self):
        #Pulls in the Celsius input (cTemp) and calculates to Fahrenheit (fTemp)
        #Returns the fTemp to the outputField
    #    cTemp = self.inputField.getNumber()
    #    fTemp = 9/5*cTemp+32
    #    self.outputField.setNumber(fTemp)

  #  def convertFtoC(self):
        #Pulls in the input (fTemp) and calculates to Celsius (cTemp)
        #Returns the cTemp to the outputField
   #     fTemp = self.inputField.getNumber()
   #     cTemp = (fTemp-32)*5/9
   #     self.outputField.setNumber(cTemp)



"""
