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

#Enigma Rotor Configurations
Rotor1 = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J'] 
Rotor2 = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E'] 
Rotor3 = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O'] 
Rotor4 = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B'] 
Rotor5 = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
Rotor6 = ['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W'] 
Rotor7 = ['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T'] 
Rotor8 = ['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V'] 

#Set of All Rotors
Enigma_Rotors = [Rotor1, Rotor2, Rotor3, Rotor4, Rotor5, Rotor6, Rotor7, Rotor8]


#Class to implement Rotors
#Rotor is Initialized with a list of letters as given and can rotate the pointer to keep track of the position
class Rotor:
    'Implement a Rotor for the Enigma Machine'
    rotorPos = 0
    def __init__(self, rotorPermutation, pos):
        self.rotorPermutation = list(rotorPermutation)
        self.rotatebyN(pos)
        self.rotorPos = pos
        self.origPos = 0
        self.rotateFlag = False #All rotors are configured to NOT rotate initially
        #print("Rotor Configuration:\n", self.rotorPermutation)

    #Function to rotate the rotor by a specified initial rotation, n
    def rotatebyN(self, n):
        for i in range(n):
            self.rotate()
        
    #Function to rotate the rotor once
    def rotate(self):
        self.rotorPos += 1 #keep track of positions
        self.rotorPos = self.rotorPos % 26
        
        #shift all elements in rotorPermutation one space to the right
        rotatedRotor = []
        for i in range(len(self.rotorPermutation)):
            rotatedRotor.append(self.rotorPermutation[(i-1)%26])
        
        #increment each character by 1
        self.rotorPermutation = [Letters[((Char_Indices[ch]) +1)%26] for indx, ch in enumerate(list(rotatedRotor))]
        #print(self.rotorPermutation)
        
    #display the Details of the rotor and its current location
    def displayRotor(self):
        print("Rotor Configuration:", self.rotorPermutation)
        print("Rotor Position:", self.rotorPos, "\nRotor Original Position:", self.origPos)
        
    #take a character as input and return its rotated ciphertext character
    #rotate rotor after encrypting automatically
    def outputRotated(self, charX):            
        #Rotate the rotor if the flag is set to true
        if(self.rotateFlag):
            self.rotate()
            
        X_index = Char_Indices[charX]
        rotatedChar = self.rotorPermutation[X_index]
            
        return rotatedChar
    
    def outputRotatedRev(self, charX):
        X_index = getIndex(charX, self.rotorPermutation)
        rotatedCharRev = Letters[X_index]
                        
        return rotatedCharRev
		


#Class to Implement a Set of Rotors along with the reflector
#Customized to build a 3-Rotor Set and Fastest moving rotor is closest to Plugboard
#Both the parameters in the init uniquely identify the rotor element of the key

class RotorSet(Rotor, Reflector):
    'Implements a Rotor Set for a 3-Rotor Enigma Machine'
    #useRotors is a list that has the index of the rotor to be used from Enigma_Rotors 
    #(Rotor1 = 0, Rotor2 = 1, ..., Rotor8 = 7)
    #rotorPositions is list with the initial position of the rotors being used
    #both the above lists are in order of closest to plugboard to furthest in terms of their rotor set position
    
    def __init__(self, useRotors, rotorPositions, reflectNum): #Instantiates the rotor set
        self.R1 = Rotor(Enigma_Rotors[useRotors[0]], rotorPositions[0]) #Rotor R1 to be placed nearest the plugboard
        self.R2 = Rotor(Enigma_Rotors[useRotors[1]], rotorPositions[1])
        self.R3 = Rotor(Enigma_Rotors[useRotors[2]], rotorPositions[2])
        
        #Instantiate correct reflector
        self.Reflector1 = Reflector(reflectNum)
        
        print("\nInitialized Enigma 3-Rotor Set with Plugboard Successfully")
        #self.R1.displayRotor()
        #self.R2.displayRotor()
        #self.R3.displayRotor()
        print("-------------------------------------------------------------------------------------------------------")

        
    #funtion to display the state of the rotor positions
    def displayRotorState(self):
        print("Current RotorState:", self.R1.rotorPos, self.R2.rotorPos, self.R3.rotorPos)
    
    #Encrypt text as per the rotor settings and spin rotors as per the gearing
    #Each rotor takes the output of the previous rotor as its input
    #The reflector and backward path has also been accomodated
    def encryptText(self, textArray):
        rotorSet_out = []
        #Only set rotate flag for R1=True since it must rotate every turn
        self.R1.rotateFlag = True
        #Traverse the array with characters once
        for indx, letter in enumerate(textArray):
            
            #self.displayRotorState() #Check Rotorstate
            #R1 always encrypts the letter and rotates
            R1out = self.R1.outputRotated(letter)
            
            '''
            #Test just one rotor + reflector
            refOut = self.Reflector1.outputReflected(R1out)
            
            R1outrev = self.R1.outputRotatedRev(refOut)
            
            print("Letter Path:", letter, " ->", R1out, " ->", refOut, " ->"
                 , R1outrev) 
            '''            
            #R2 is configured to rotate every time R1 completes a cycle, except first index
            if(self.R1.rotorPos == ((self.R1.origPos)%26) and indx != 0 ):
                self.R2.rotateFlag = True
            
            R2out = self.R2.outputRotated(R1out)
            
            #R3 is configured to rotate every time R3 completes a cycle, except first cycle
            if(self.R2.rotorPos == ((self.R2.origPos)%26) and self.R2.rotateFlag and indx > 26):
                self.R3.rotateFlag = True
                
            R3out = self.R3.outputRotated(R2out)
                
            #Pass through reflector
            reflectedOut = self.Reflector1.outputReflected(R3out)
            
            #Pass through R3 again
            R3out_rev = self.R3.outputRotatedRev(reflectedOut)
            self.R3.rotateFlag = False #Rotate flag must stay false as default

            #Pass through R2 again
            R2out_rev = self.R2.outputRotatedRev(R3out_rev)
            self.R2.rotateFlag = False #Rotate flag must be set to false as default
            
            R1out_rev = self.R1.outputRotatedRev(R2out_rev)
            
            #print path of letter:
            #print("Letter Path:", letter, " ->", R1out, " ->", R2out, " ->", R3out, " ->", reflectedOut, " ->"
                 #, R3out_rev, " ->", R2out_rev, " ->", R1out_rev)
            #The character stored in R1out_rev is the final result of rotors + reflector

            rotorSet_out.append(R1out_rev)
        
        
        return rotorSet_out
    