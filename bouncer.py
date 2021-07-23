from midiutil import MIDIFile
import math

#Standard Defaults
bHeight = 127
bLoss = .75
bTime = 0 
gravity = 32
lowestNote = 0

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

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

MyMIDI.addNote(track,channel,bHeight,time,duration,volume)
time = calcTime(bHeight,gravity)
MyMIDI.addNote(track,channel,0,time,duration,volume)

for i in range(1,32):
	bHeight = calcLoss(bHeight,bLoss)
	time = time + calcTime(bHeight,gravity)
	MyMIDI.addNote(track,channel,math.floor(bHeight),time,duration,volume)
	time = time + calcTime(bHeight,gravity)
	MyMIDI.addNote(track,channel,0,time,duration,volume)

with open("output.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)

