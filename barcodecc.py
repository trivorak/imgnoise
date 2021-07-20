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
controllerNumber = 55

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

#Get Color Funtion
def getColor(w,h):
	return im.getpixel((w,h))

# Open Image and get size
im = Image.open('output.png');
width , height = im.size;

# Main Loop
for y in range(0,height):
	for x in range(0, width):
		if (getColor(x,y) < 1):
			MyMIDI.addControllerEvent(track,channel,time, controllerNumber, 127)
		if (getColor(x,y) > 1):
			MyMIDI.addControllerEvent(track,channel,time, controllerNumber, 0)
		time = time + duration*countingVar
		countingVar = 1
	time = 0

# Write Midi file
with open("barcodecc.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)