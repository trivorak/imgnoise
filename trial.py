from PIL import Image
from midiutil import MIDIFile

#Variable Defaults
countingVar = 1

#Midi Defaults
track = 0
channel = 0
time = 0
duration = 0.25
tempo = 110
volume = 100

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

#Get Color Funtion
def getColor(w,h):S
	return im.getpixel((w,h))

# Open Image and get size
im = Image.open('output.png');
width , height = im.size;

# Main Loop
for y in range(0,height):
	for x in range(0, width):
		if (x+1 < width and getColor(x,y) == getColor(x+1,y)):
			countingVar = countingVar + 1
			continue
		if (getColor(x,y) < 1):
			MyMIDI.addNote(track,channel,abs(-127+y),time, duration*countingVar, volume)
		time = time + duration*countingVar
		countingVar = 1
	time = 0

# Write Midi file
with open("output.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)