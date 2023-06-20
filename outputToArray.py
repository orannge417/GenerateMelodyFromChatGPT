def outputToArray(Output):
    lyricsArray = []
    lyricsBool = False
    lyricsCount = 0

    keyArray = []
    keyBool = False
    keyCount = -1

    for char in Output:
        if(char == '"' and lyricsBool == False):
            lyricsBool = True
            lyricsArray.append('')
            keyCount += 1
            continue
        elif (char == '"'):
            lyricsBool = False
            lyricsCount += 1
            keyBool = True
            keyArray.append('')
            continue

        if (lyricsBool == True):
            lyricsArray[lyricsCount] += char

        if (keyBool == True and char == "|"):
            keyBool = False
        elif (keyBool == True and char != " "):
            keyArray[keyCount] += char

    print(lyricsArray, keyArray)
    return(lyricsArray, keyArray)
