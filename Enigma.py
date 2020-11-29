#Karan Vombatkere
#German Enigma Machine
#October 2017

from string import *
import numpy as np

#Import Enigma components
from Plugboard import *
from Reflector import *
from Rotorset import *

Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#function to create a dictionary with letters and their indices
#Use this to return the index of a letter (a = 0, .., z = 25)
def genDictionary():
    letter_index_pairs = []
    for indx, char in enumerate(Letters):
        letter_index_pairs.append([char, indx])

    Indx_Dict = dict(letter_index_pairs)
    print("Generated Letter Dictionary!")
    return Indx_Dict

#Call the function to create a global dictionary
Char_Indices = genDictionary()

#Function to check if a character exists in a string/array
def checkMatch(str1, char1):
    for i in range(len(str1)):
        if(str1[i] == char1):
            return True
          
    return False

#Function to return the index of a letter (a = 0, .., z = 25)
#StringA would be Letters when calling this function
def getIndex(char, stringA):
    for i in range(len(stringA)):
        if (char == stringA[i]):
            return i
        
    return None
	
	
#Class for the Enigma machine
#Takes a text string as an input and returns the corresponding encrypted/decrypted string
class Enigma(RotorSet, Plugboard):
    'Implementation of the Enigma Machine using the Plugboard and Rotorset'
    #rotors - indices of rotors to be used from Enigma_Rotors
    #rotorPos - Initial positions of each of the rotors
    #refNum - index of reflector to be used from Enigma_Reflectors
    
    def __init__(self, rotors, rotorPos, refNum, plugboardSwaps):
        print("============================Enigma Machine Successfully Initialized======================================\n")
        self.rSet = RotorSet(rotors, rotorPos, refNum)
        self.pBoard = Plugboard()
        self.pBoard.setPBKey(plugboardSwaps)
        self.rotorList = list(rotors)
        self.displayKey() #display the current key
        print("============================Enigma Machine Successfully Initialized======================================\n")
    
    
    #Function to display current settings of Enigma
    def displayFullSettings(self):
        print("==============================Current Settings of Enigma Machine======================================\n")
        self.rSet.R1.displayRotor()
        self.rSet.R2.displayRotor()
        self.rSet.R3.displayRotor()
        self.rSet.displayRotorState()

        self.pBoard.displayPB()
        self.rSet.Reflector1.displayReflector()
        
        
    #Function to set the key of the Enigma
    def setKey(self, rotors, rotorPos, refNum, plugboardSwaps):
        self.rSet = RotorSet(rotors, rotorPos, refNum)
        self.rotorList = list(rotors)
        
        self.pBoard = Plugboard()
        self.pBoard.setPBKey(plugboardSwaps)
        #self.displayKey() #display settings to verify
        
    
    def displayKey(self):
        print("-----------------------------------------------------------------------------------------------------------")
        print("Displaying Current Key Settings:")
        print("Rotors Selected (from nearest to Plugboard):", self.rotorList)
        print("Rotor Current Positions (from nearest to Plugboard): |Rotor1 =", self.rSet.R1.rotorPos, 
              "|Rotor2 =", self.rSet.R2.rotorPos, "|Rotor3 =", self.rSet.R3.rotorPos, "|")
        self.pBoard.displayPB()
        self.rSet.Reflector1.displayReflector()
        print("-----------------------------------------------------------------------------------------------------------")

    
    #Run the Enigma on text
    def runEnigma(self, textStr):
        #first process text, by removing special characters and spaces, etc and capitalizing
        charCount = 0
        textStr = textStr.upper()
        cleanText = ''
        for i, char in enumerate(textStr):
            if(checkMatch(Letters, char)):
                cleanText += char
                charCount += 1
                
        print("======================================RUNNING ENIGMA CIPHER================================================")
        print("Running Enigma Cipher on following Text Input (Character Count =",charCount,"):\n", cleanText)
                
        #Mechanics of the Enigma : Plugboard -> 3 Rotors -> Reflector -> 3 Rotors -> Plugboard
        #The 3 Rotors are in order from R1 -> R2 -> R3, where R1 is nearest plugboard and spins the fastest
        #Note that the rotors turn once (according to the gears) after each letter is encrypted
        
        #Send text string through the Plugboard
        plugboardOut = self.pBoard.outputSwapped(cleanText) #Takes string input -> Returns array output
        
        #Process text throgh Rotors and Reflectors 
        #Rotors turn within execution
        rotorsetOut = self.rSet.encryptText(plugboardOut) #Takes array input -> Returns array output
        
        #Pass the text through the reverse plugboard again
        outText = self.pBoard.reverseSwapped(rotorsetOut) #Takes array input -> Returns string output
        
        print("============================================ENIGMA OUTPUT==================================================")
        print("Output Text:\n", outText)
        
        return outText    


