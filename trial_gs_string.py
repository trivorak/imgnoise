from PIL import Image
from midiutil import MIDIFile
import math

#Variable Defaults
chordNoteCount = 5

#Midi Defaults
track = 0
channel = 0
time = 0
duration = 0.25
tempo = 110
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

# Open Image and get size / Convert to greyscale
im = Image.open('output.png');
width , height = im.size;
divisor = math.floor(height/128)
im = im.convert(mode='L')
im = im.resize((math.floor(width/divisor),math.floor(height/divisor)))
width , height = im.size;

#Used for Chord Building Finds Area of Image
#Divides the Area by number of notes you want in a chord

imageArea = width * height
loopback = math.floor(imageArea / chordNoteCount)
loopdivision = loopback*duration


for y in range(0,height):
	for x in range(0, width):
		colorValue=im.getpixel((x,y))
		if (colorValue > 0):
			MyMIDI.addNote(track,channel,math.ceil(colorValue/2),time, duration, volume)
		time = time + duration
		if (time > loopdivision):
			time = 0

with open("output.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)
