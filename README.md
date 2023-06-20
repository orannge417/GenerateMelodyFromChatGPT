Run on linux(ubuntu distribution)

Setups:

pip install requirements.txt

sudo add-apt-repository ppa:mscore-ubuntu/mscore3-stableapt update
sudo apt install musescore3
sudo ln -s /usr/bin/musescore3 /usr/bin/musescore

python3 main.py
- Please input the abc-Notation outputted from chatGPT:
For this input please input abc-Notation in the following format (you can use the following as a toy-case) 
        "we've" A4 | "made" G4 | "it," E4 | "Cele" D4 | "brate" E4 | "this" D4 | "day," C4 | "To" G4 | "new" A4 | "begin" G4 | "nings," E4 | "March" D4 | "on" E4 | "our" D4 | "way." C4 |
- Name of the txt file: 
test
- Name of the midi file: 
test

python3 -m midi2voice -l output/test.txt -m output/test.midi -g female -t 96  
