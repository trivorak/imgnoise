from PIL import Image
from midiutil import MIDIFile
import math

track = 0
channel = 0
time = 0
duration = 0.25
tempo = 110
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

im = Image.open('swing.png');
# print(im.getpixel((1,2)));
width , height = im.size;
# print(width)
# print(height)

for y in range(1,width):
	for x in range(1, height):
		# print(im.getpixel((y,x)))
		if (im.getpixel((y,x)) < 128):
			MyMIDI.addNote(track,channel,abs(-128+x),time, duration, volume)
	time = time + 0.25

with open("trial.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)