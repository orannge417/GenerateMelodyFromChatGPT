Run on linux(ubuntu distribution)

Setups:
1. Create "output" folder

2. Use below commands on terminal
pip install requirements.txt

sudo add-apt-repository ppa:mscore-ubuntu/mscore3-stableapt update
sudo apt install musescore3
sudo ln -s /usr/bin/musescore3 /usr/bin/musescore

3. On ChatGPT generate abc Notation with following prompt:
Create melody. The area enclosed in | is a single note. Place the chord progression and length of sound inside the | and enclose the chord in " ". This is the main topic. The genre of the song should be rock style. The total length of the song should be 150 measures. Length of 600 in 4-beat equivalents. This commitment is also important as it relates to the length of the song. The number of notes should be normal and the movement of the note process should be normal for the song. Please make it without rests. Also provide the tonic.
 [Summary] You are an excellent melody maker. You have invented a melody and length, and you can express a single note with | “pitch” note | such as | “C4” 4 |, | “D#5” 16 |, | “Gb6” 2 |, | “C4” 1 |. Another important rule is to enclose only the pitches in ". The first parameter is a pitch symbol, such as C4, D#5, Gb6. The second parameter is a length of sound, where 1=whole note, 2=half note, 4=quarter note, 8=eighth note, 16= sixteenth note. The format of this data is of paramount importance since your answers will be used in the program. Generate the output in single line. 

4. Run python code with following:

python3 main.py
- | "C4" 4 | "D4" 4 | "E4" 8 | "F4" 8 | "G4" 4 | "A4" 4 | "B4" 4 | "C5" 4 | "D5" 8 | "E5" 8 | "F5" 4 | "G5" 4 | "A5" 8 | "B5" 8 | "C5" 4 | "D5" 4 |
- Name of the txt file: 
test
- Name of the midi file: 
test

