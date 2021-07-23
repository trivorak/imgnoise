from midiutil import MIDIFile
import math

#Standard Defaults
bHeight = 127
bLoss = .75
bTime = 0 
gravity = 32
highestNote = 127
lowestNote = 30

#Midi Defaults
track = 0
channel = 0
time = 0
duration = 0.25
tempo = 110
volume = 100
note = 32

# Define Functions
def calcTime(h,g):
	return math.sqrt(2*h/g)

def calcLoss(h,l):
	return h*l

# Scale Range to Note Range
def scaleRange(h,l):
	return math.floor(h*l)

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

noteRange = highestNote - lowestNote

MyMIDI.addNote(track,channel,highestNote,time,duration,volume)
time = calcTime(bHeight,gravity)
MyMIDI.addNote(track,channel,lowestNote,time,duration,volume)

while math.floor(bHeight)>1:
	bHeight = calcLoss(bHeight,bLoss)
	time = time + calcTime(bHeight,gravity)
	noteRange = scaleRange(noteRange,bLoss)
	MyMIDI.addNote(track,channel,noteRange+lowestNote,time,duration,volume)
	time = time + calcTime(bHeight,gravity)
	MyMIDI.addNote(track,channel,lowestNote,time,duration,volume)

with open("bounce.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)

