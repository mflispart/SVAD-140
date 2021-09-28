from breezypythongui import EasyFrame
from tkinter import PhotoImage
#from tkinter.font import font
import random

class PFSCharacterCreator(EasyFrame):
    #Program for creating a Pathfinder Society (PFS) character

    def __init__(self):
        #Sets up the window, label, and button.
        EasyFrame.__init__(self, width = 1024, height = 768, title = "PFS Character Creator")
        #Window setup for width, height, and title bar in Window

        #Set Labels, boxes, and buttons
        self.addLabel(text = "Pathfinder Society Character Creator", row = 0, column = 0, columnspan = 1, rowspan = 1, sticky = "NW")
        self.addLabel(text = "Character Name: ", row = 1, column = 0, columnspan = 1, rowspan = 1,sticky = "NW")
        self.charName = self.addTextField(text = "Character Name",
                                            row = 2,
                                            column = 0,
                                            width = 25,
                                            columnspan = 1,
                                            rowspan = 1,
                                            sticky = "NW")
        
        self.addButton(text = "Select Character Class", row = 3, column = 0, columnspan = 1, command = self.classSelect)
        
        self.charClass = self.addTextField(text = "Character Class", row = 4, column = 0, width = 25, columnspan = 1, rowspan = 1, sticky = "NW", state = "readonly")

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

             
        #Testing panels for future use
        #dataPanel = self.addPanel(row = 0, column = 1, background = "gray")
        #dataPanel.addLabel(text = "Label 1", row = 1, column = 1)
        #dataPanel.addTextField(text = "Text1", row = 1, column = 2)
        #dataPanel.addLabel(text = "Label 2", row = 2, column = 2)
        #dataPanel.addTextField(text = "Text1", row = 2, column = 2)

    #Testing a pop-up box for Class Selection with a Radio Button list
    #Current test is using promptString and returns charClass to Output Field
    def classSelect(self):
        charClass = self.prompterBox(title = "Select your Character Class", promptString = "Class")
        self.charClass.setText(charClass)

    #Die Roller - ranges for each game die set - 20 sided (most common at top),
    #100 sided, 12 sided, 10 sided, 8, 6, 4, and 2 sided.
    def rollD20(self):
        d20 = random.randint(1,20)
        self.outputFieldDieRoll.setNumber(d20)
    def rollD100(self):
        d100 = random.randint(1,100)
        self.outputFieldDieRoll.setNumber(d100)
    def rollD12(self):
        d12 = random.randint(1,12)
        self.outputFieldDieRoll.setNumber(d12)
    def rollD10(self):
        d10 = random.randint(1,10)
        self.outputFieldDieRoll.setNumber(d10)
    def rollD8(self):
        d8 = random.randint(1,8)
        self.outputFieldDieRoll.setNumber(d8)
    def rollD6(self):
        d6 = random.randint(1,6)
        self.outputFieldDieRoll.setNumber(d6)
    def rollD4(self):
        d4 = random.randint(1,4)
        self.outputFieldDieRoll.setNumber(d4)
    def rollD2(self):
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
