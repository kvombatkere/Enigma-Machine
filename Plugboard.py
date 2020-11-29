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

#Class to implement Plugboard
#Plugboard takes a string input (spaces, special characters removed) and Returns a list after swapping characters
#Implements both forward and reverse swaps of characters
class Plugboard:
    'Class to implement plugboard for the German Enigma Machine'
    Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    initConfig = Letters

    #Initialize Plugboard with a particular configuration
    def __init__(self):
        self.configList = list(Plugboard.initConfig)
        #print("Plugboard Initialized (No Letters Swapped) - Please Set Key: \n", self.configList)
        
    #function to swap a pair of characters in a list
    #indx_list is a list with two values
    def swapPair(self, indx_list, List1):
        a = indx_list[0]
        b = indx_list[1]
        
        tmp = List1[a]
        List1[a] = List1[b]
        List1[b] = tmp
        return List1

    #set the plugboard key
    #function to swap all the characters specified by a 2D list defining the swaps
    def swapChars(self, indx_2Dlist):
        for i, chars in enumerate(indx_2Dlist): #chars is a tuple with 2 letters
            indx1 = Char_Indices[chars[0]]
            indx2 = Char_Indices[chars[1]]
            self.swapPair([indx1, indx2], self.configList)
            #print("Plugboard characters", chars[0], "and", chars[1], "were successfully swapped")
            
        return self.configList
    
    
    #function to set the plugboard key
    def setPBKey(self, swapList): 
        self.configList = list(Plugboard.initConfig) #reset plugboard before implementing swapping sequence
        self.swapChars(swapList)       
        #self.displayPB() #Display the current key setting
        
    #function to display the plugboard settings
    def displayPB(self):
        print("Displaying Current Plugboard Configuration with letter swaps:", self.configList)
        
    #Takes a string/list input of characters to be swapped
    #Returns an array as the output
    def outputSwapped(self, charsX):
        PBswapped_chars = []
        for i, char in enumerate(charsX):
            orig_indx = Char_Indices[char]
            PBswapped_chars.append(self.configList[orig_indx])
        
        #print("Message Output after plugboard swaps: ", PBswapped_chars)
        return PBswapped_chars
    
    def reverseSwapped(self, charsX):
        PBreverseSwapped = ""
        for i, char in enumerate(charsX):
            pb_indx = getIndex(char, self.configList)
            PBreverseSwapped += Letters[pb_indx]
        
        #print("Output after plugboard Reverse swaps: ", PBreverseSwapped)
        return PBreverseSwapped
		



