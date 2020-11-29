#Karan Vombatkere
#German Enigma Machine
#October 2017


#Function to test the rotor settings with a crib - some kind of bombe simulator
#Use an index/counter value to keep track of match rate, since plugboard will reduce matches.
#Output rotor settings with highest match rates.
#Input: Takes a crib and ptext as input
#Output: Returns Rotor settings with highest match rate (after trying all 17576 settings)

def findRotorPos(crib, ptext):
    #Convert crib to uppercase for comparison
    crib = crib.upper()
    
    #Possible Rotor position setting array
    rotorPosGuess = []
    rotorCombination = []
    settingNo = 0
    
    #Outermost loop to test 6 different rotor combinations
    for c1 in range(3):
        for c2 in range(3):
            for c3 in range(3):
                
                if(c1 != c2 and c1 != c3 and c2 != c3): #if statement to only check different rotor combinations
                    print('Checking all 17576 Initial Settings for Rotor Combinations:', c1, c2, c3,'...')
                    
                    #Use 3 inner for loops to try all 17576 initial settings
                    for a in range(26):
                        for b in range(26):
                            for c in range(26):

                                #settingNo += 1
                                #print("Checking Rotor Setting #", settingNo, "-",a,b,c)

                                #Instantiate Enigma Machine without any Plugboard swaps, Reflector B, 0, 0, 0 initial pos
                                enigmaTest = Enigma([c1, c2, c3], [a, b, c], 0, [])
                                #Reset the matchRate to 0
                                matchRate = 0

                                for i in range(len(ptext)):
                                    cipherLetter = enigmaTest.runEnigma(ptext[i])
                                    #Letter should equal the crib character and not be the same as the original
                                    if(cipherLetter == crib[i] and cipherLetter != ptext[i]):
                                        matchRate += 1 #Increment if a match is found

                                if(matchRate > 14): #Greater than 30% matches
                                    rotorPosGuess.append([a,b,c])
                                    rotorCombination.append([c1,c2,c3])
                                    print("Match Rate =", matchRate)
                                    #return rotorPosGuess #return match if it is found (stop machine equivalent)
   
    return rotorPosGuess, rotorCombination