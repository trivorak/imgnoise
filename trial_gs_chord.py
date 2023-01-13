from PIL import Image
from midiutil import MIDIFile
import math

#Midi Defaults
track = 0
channel = 0
time = 0
duration = 1.0
tempo = 110
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

# Open Image and get size
im = Image.open('output.png');
width , height = im.size;

# Used for Chord Building Finds Area of Image
# Divides the Area by number of notes you want in a chord
# Need to add Chord Range
imageArea = width * height
loopback = width
loopdivision = loopback*duration

# Sets Range of Chords. Set OctaveRange and leave RangeMath alone
octaveRange = 4
rangeMath = (octaveRange*12)/128

for y in range(0,height):
	for x in range(0, width):
		colorValue=im.getpixel((x,y))
		if (colorValue > 0):
			MyMIDI.addNote(track,channel,math.ceil(rangeMath*(colorValue/2)),time, duration, volume)
		time = time + duration
		if (time > loopdivision):
			time = 0

with open("output.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)
