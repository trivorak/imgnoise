from PIL import Image

# Define List
normList = []

# Open Image and get size
im = Image.open('output.png');
width , height = im.size;

# Main Loop
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

