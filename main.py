# output Template: 
# | "C4" 4 | "D4" 4 | "E4" 8 | "F4" 8 | "G4" 4 | "A4" 4 | "B4" 4 | "C5" 4 | "D5" 8 | "E5" 8 | "F5" 4 | "G5" 4 | "A5" 8 | "B5" 8 | "C5" 4 | "D5" 4 |


from outputToArray import outputToArray
from music21Midi import outputMidi

if __name__ == '__main__' :
    output = input("Please input the abc-Notation outputted from chatGPT\n")
    
    midiName = "output//" + input("Name of the midi file: \n") + ".midi"

    keyArray, rhythmArray = outputToArray(output)

    outputMidi(rhythmArray, keyArray, midiName)
    
