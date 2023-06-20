def outputTxt(lyricsArray, txtName):
    

    with open(txtName, "w") as txt_file:
        for line in lyricsArray:
            txt_file.write(" ".join(line) + "\n")