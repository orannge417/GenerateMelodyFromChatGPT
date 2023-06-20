# https://qiita.com/iNomaG/items/16081daf103a042ea0fe

from music21 import *


def outputMidi(keyArray, midiName):

    score = stream.Score()
    notes = []

    for key in keyArray:
        n = note.Note(key)
        n.duration.type = 'half'
        notes.append(n)

    score.append(notes)

    fp = score.write('midi', midiName)