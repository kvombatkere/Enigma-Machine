#Karan Vombatkere
#German Enigma Machine
#October 2017

from string import *
import numpy as np

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


#Enigma Reflectors
Refl_B = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T'] 
Refl_C = ['F','V','P','J','I','A','O','Y','E','D','R','Z','X','W','G','C','T','K','U','Q','S','B','N','M','H','L'] 

Enigma_Reflectors = [Refl_B, Refl_C]

#Class to Implement Reflector
class Reflector:
    'Reflector implementation for Enigma Machine'
    #Takes a number useReflector as an input, which corresponds to the reflector index in Enigma_Reflectors
    def __init__(self, useReflector):
        self.Refl = list(Enigma_Reflectors[useReflector])
        #print("Reflector Successfully selected:", self.Refl)

    #function to display the reflector
    def displayReflector(self):
        print("Reflector selected:", self.Refl)
        
    #function to output the reflected letter as per the Reflector
    def outputReflected(self, charX):
        X_index = Char_Indices[charX]
        reflectedChar = self.Refl[X_index]
        
        return reflectedChar