from midiutil import MIDIFile
import math

# Ref Length Math
# Round((input / 255) / 128 ) * 128 * 4
# If above = 0 then + 1/128

# Variabel Defaults
chordNoteCount = 3
octaveRange = 5

with open("input.txt","r") as f:
    a = f.read()

# Remove Carriage Returns
a = a.replace('\n','')

#Convert to string
a = str(a)

# Create blank list
aList = []
aListInt = []

# Split by every 2 characters and append to "blank list"
for i in range(0,len(a),2):
    aList.append(a[i:i+2])

# Loop hex to int into new list
for element in aList:
    aListInt.append(int(element,16))

# Duration Function
def getDuration(noteDuration):
    return round((noteDuration / 255) * 128) / 128 * 4

# Midi Defaults
track = 0
channel = 0
time = 0
duration = 0.50
tempo = 80
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

loopback = math.floor((len(aListInt)/ chordNoteCount))
note = 0
noteRange = (octaveRange * 12) / 128

print(len(aListInt))
print(len(aListInt)%3)

# Make Sure List is divisible by 4
# If not append to list
for i in range(0,3-len(aListInt)%3):
	aListInt.append(0)

print(len(aListInt))
print(len(aListInt)%4)

for i in range(0,len(aListInt),3):
    noteLength = getDuration(aListInt[i+1])
#    noteGap = getDuration(aListInt[i+3])/4
    noteGap = 0

    if (noteLength == 0):
        noteLength = 1/32

    print(math.ceil(noteRange*(aListInt[i]/2)))
    MyMIDI.addNote(track,channel,math.ceil(noteRange*aListInt[i]/2),time,noteLength,math.ceil(aListInt[i+2]/2))
    time = time + noteLength + noteGap
    note = note + 1
    if (note > loopback):
        time = 0
        note = 0


with open("output_hex.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)
