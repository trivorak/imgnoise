from PIL import Image
from midiutil import MIDIFile

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

for y in range(1,width):
	for x in range(1, height):
		if (im.getpixel((y,x)) < 128):
			MyMIDI.addNote(track,channel,abs(-128+x),time, duration, volume)
	time = time + 0.25

with open("output.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)