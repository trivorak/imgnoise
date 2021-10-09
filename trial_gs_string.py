from PIL import Image
from midiutil import MIDIFile
import math

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
im = im.convert(mode='L')

for x in range(0,height):
	for y in range(0, width):
		colorValue=im.getpixel((y,x))
		colorValue = 255-colorValue
		if (colorValue > 0):
			MyMIDI.addNote(track,channel,math.ceil(colorValue/2),time, duration, volume)
		time = time + 0.25

with open("output.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)
