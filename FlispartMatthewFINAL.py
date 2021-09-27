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
        
        self.charClass = self.addTextField(text = "Character Class",
                                            row = 4,
                                            column = 0,
                                            width = 25,
                                            columnspan = 1,
                                            rowspan = 1,
                                            sticky = "NW",
                                            state = "readonly")


             
        #Testing panels for future use
        dataPanel = self.addPanel(row = 0, column = 1, background = "gray")
        dataPanel.addLabel(text = "Label 1", row = 1, column = 1)
        dataPanel.addTextField(text = "Text1", row = 1, column = 2)
        dataPanel.addLabel(text = "Label 2", row = 2, column = 2)
        dataPanel.addTextField(text = "Text1", row = 2, column = 2)

    #Testing a pop-up box for Class Selection with a Radio Button list
    #Current test is using promptString and returns charClass to Output Field
    def classSelect(self):
        charClass = self.prompterBox(title = "Select your Character Class", promptString = "Class")
        self.charClass.setText(charClass)
        
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
