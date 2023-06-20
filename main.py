# output Template: 
# "we've" A4 | "made" G4 | "it," E4 | "Cele" D4 | "brate" E4 | "this" D4 | "day," C4 | "To" G4 | "new" A4 | "begin" G4 | "nings," E4 | "March" D4 | "on" E4 | "our" D4 | "way." C4 |

from outputToArray import outputToArray
from outputLyrics import outputTxt
from music21Midi import outputMidi

if __name__ == '__main__' :
    output = input("Please input the abc-Notation outputted from chatGPT\n")
    
    txtName = "output//" + input("Name of the txt file: \n") + ".txt"
    midiName = "output//" + input("Name of the midi file: \n") + ".midi"

    lyricsArray, keyArray = outputToArray(output)

    outputTxt(lyricsArray, txtName)
    outputMidi(keyArray, midiName)
    
