import random

notes = {
    "C" : 0,
    "C#" : 1,
    "D" : 2,
    "D#" : 3,
    "E" : 4,
    "F" : 5,
    "F#" : 6,
    "G" : 7,
    "G#" : 8,
    "A" : 9,
    "A#" : 10,
    "B" : 11,
}

intervals = {
    "m2" : 1,
    "M2" : 2,
    "m3" : 3,
    "M3" : 4,
    "P4" : 5,
    "TT" : 6,
    "P5" : 7,
    "m6" : 8,
    "M6" : 9,
    "m7" : 10,
    "M7" : 11,
}

def getNote(note, interval):
    position = notes[note]
    return list(notes)[(position + intervals[interval]) % 12]

while True:
    rn = random.choice(list(notes))
    ri = random.choice(list(intervals))
    correct = getNote(rn, ri)
    print(rn + " " + ri)
    if (input() == correct):
        print("Correct!")
    else:
        print("The correct answer is " + correct)