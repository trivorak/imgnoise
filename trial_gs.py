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

# Open Image and get size
im = Image.open('input.png');
width , height = im.size;

for y in range(0,width):
	for x in range(0, height):
				red, green, blue, alpha = im.getpixel((y,x))
				red = 255-red
				if (red > 0):
					MyMIDI.addNote(track,channel,abs(-127+x),time, duration, math.ceil(red/2))
	time = time + 0.25

with open("output.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)
