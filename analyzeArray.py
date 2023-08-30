def TwoRepetitions(notes, durations):
    # notesとdurationsの連続する2つの要素のペアをリストにする
    pairs = [(notes[i], durations[i], notes[i+1]) for i in range(len(notes) - 1)]

    # 各ペアが何回繰り返されているかを計算
    pair_counts = {}
    for pair in pairs:
        if pair in pair_counts:
            pair_counts[pair] += 1
        else:
            pair_counts[pair] = 0

    TotalCount = 0
    # 繰り返し回数を出力
    for pair, count in pair_counts.items():
        note1, duration1, note2 = pair
        TotalCount += count
        # print(f"Pair ({note1}, {duration1}) -> ({note2}, *): Repeated {count} times")

    return TotalCount

def ThreeRepetitions(notes, durations):

    # notesとdurationsの連続する3つの要素の組み合わせをリストにする
    # 最後のアイテムのdurationは考慮しない
    triplets = [(notes[i], durations[i], notes[i+1], durations[i+1], notes[i+2]) for i in range(len(notes) - 2)]

    # 各組み合わせが何回繰り返されているかを計算
    triplet_counts = {}
    for triplet in triplets:
        if triplet in triplet_counts:
            triplet_counts[triplet] += 1
        else:
            triplet_counts[triplet] = 0

    TotalCount = 0
    # 繰り返し回数を出力
    for triplet, count in triplet_counts.items():
        note1, duration1, note2, duration2, note3 = triplet
        TotalCount += count
        # print(f"Triplet ({note1}, {duration1}) -> ({note2}, {duration2}) -> ({note3}, *): Repeated {count} times")

    return TotalCount

def note_to_value(note):
    mapping = {
        'C3': -12, 'C#3': -11, 'Db3': -11, 'D3': -10, 'D#3': -9, 'Eb3': -9,
        'E3': -8, 'F3': -7, 'F#3': -6, 'Gb3': -6, 'G3': -5, 'G#3': -4,
        'Ab3': -4, 'A3': -3, 'A#3': -2, 'Bb3': -2, 'B3': -1,
        'C4': 0, 'C#4': 1, 'Db4': 1, 'D4': 2, 'D#4': 3, 'Eb4': 3,
        'E4': 4, 'F4': 5, 'F#4': 6, 'Gb4': 6, 'G4': 7, 'G#4': 8,
        'Ab4': 8, 'A4': 9, 'A#4': 10, 'Bb4': 10, 'B4': 11, 'C5': 12,
        'C#5': 13, 'Db5': 13, 'D5': 14, 'D#5': 15, 'Eb5': 15, 'E5': 16,
        'F5': 17, 'F#5': 18, 'Gb5': 18, 'G5': 19, 'G#5': 20, 'Ab5': 20,
        'A5': 21, 'A#5': 22, 'Bb5': 22, 'B5': 23, 'C6': 24, 'C#6': 25,
        'Db6': 25, 'D6': 26, 'D#6': 27, 'Eb6': 27, 'E6': 28, 'F6': 29,
        'F#6': 30, 'Gb6': 30, 'G6': 31, 'G#6': 32, 'Ab6': 32, 'A6': 33,
        'A#6': 34, 'Bb6': 34, 'B6': 35, 'C7': 36
    }
    return mapping[note]

def average_tonal_distance(notes):
    total_distance = 0

    for i in range(1, len(notes)):
        total_distance += abs(note_to_value(notes[i]) - note_to_value(notes[i-1]))

    return total_distance / (len(notes) - 1)


def SongLength(durations):
    Length = 0
    for duration in durations:
        Length += 1/int(duration)
    
    return Length


def analyzeArray(keyArray, rhythmArray):
    TwoRepCount = TwoRepetitions(keyArray, rhythmArray)
    ThreeRepCount = ThreeRepetitions(keyArray, rhythmArray)
    TonalDist = average_tonal_distance(keyArray)
    SongLen = SongLength(rhythmArray)

    print("Two Repetitions: ", TwoRepCount)
    print("Three Repetitions: ", ThreeRepCount)
    print("Avg Tonal Distance: ", TonalDist)
    print("Note variation: ", len(set(keyArray)))
    print("Duration variation: ", len(set(rhythmArray)))
    print("Song Length: ", SongLen)