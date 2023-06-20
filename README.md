Run on linux(ubuntu distribution)

Setups:
Create "output" folder

pip install requirements.txt

sudo add-apt-repository ppa:mscore-ubuntu/mscore3-stableapt update
sudo apt install musescore3
sudo ln -s /usr/bin/musescore3 /usr/bin/musescore

python3 main.py
- Please input the abc-Notation outputted from chatGPT:
For this input please input abc-Notation in the following format (you can use the following as a toy-case) 
    | "We" C4 | "have" D4 | "come" E4 | "so" F4 | "far" G4 | "my" A4 | "dear" G4 | "friends" F4 | "Shared" E4 | "laughs" D4 | "and" E4 | "shed" F4 | "our" G4 | "tears" A4 | "in" G4 | "School" E4 | "of" D4 | "life" E4 | "we" F4 | "made" G4 | "it" A4 | "through" G4 | "the" F4 | "Years" E4 | "now" D4 | "it’s" E4 | "time" F4 | "to" G4 | "say" A4 | "good" G4 | "bye" F4 |
- Name of the txt file: 
test
- Name of the midi file: 
test

python3 -m midi2voice -l output/test.txt -m output/test.midi -g female -t 96  
