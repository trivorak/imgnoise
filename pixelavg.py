from PIL import Image
from midiutil import MIDIFile
import math

#Generic Variable
colorValAvg = 0

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
im = Image.open('output.png');
width , height = im.size;

for x in range(0,width):
    for y in range(0, height):
        colorValue=im.getpixel((x,y))
        colorValue = 255-colorValue
        colorValAvg = colorValAvg + colorValue
    colorValAvg = colorValAvg / (height*2)
    MyMIDI.addNote(track,channel,math.ceil(colorValAvg/2),time, duration, volume)
    time = time + 0.25
    colorValAvg = 0

with open("pixelavg.mid","wb") as output_file:
    MyMIDI.writeFile(output_file)
