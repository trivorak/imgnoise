from PIL import Image
from midiutil import MIDIFile

# Define List
normList = []

# Open Image and get size
im = Image.open('output.png');
width , height = im.size;

# Main Input Loop
for y in range(0,width):
	for x in range(0, height):
		colorValue=im.getpixel((y,x))
		colorValue = colorValue / 255
		normList.append(colorValue)

print(normList)

myFile=open('output.norm','w')

for element in normList:
	myFile.write(str(element))
	myFile.write('\n')

myFile.close()

#///////////////////////// 
# Main Output Loop  //////
#/////////////////////////

# Define Midi Defaults
track = 0
channel = 0
time = 0
duration = 0.25
tempo = 110
volume = 100
controllerNumber = 55

# Init Midi File
MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track,time,tempo)

# Output translation

for element in normList:
	MyMIDI.addNote(track,channel,round(element*127),time,duration,volume)
	time = time + 0.25

# Write Midi file
with open("libtest.mid","wb") as output_file:
	MyMIDI.writeFile(output_file)