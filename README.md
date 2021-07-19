# imgnoise
This project uses a similar concept to music16 but it takes a black and white image and maps the pixels to a midi file.

#### Why is this getting built?
Music experiments.

### Requirements
- `Python3`
- `PIL`
- `MIDIUTIL` 
install MIDIUTIL with `pip install -r requirements.txt`

## What the code needs
The current code takes a black and white image and converts the pixel information into midi information. 
As the midi standard is 128 notes max you must convert an image into a 128 tall image.

## How to use (for future me)
If you have imagemagick installed on your computer run the command 

#### Windows
**`magick input.jpg -filter point -monochrome -resize 1000x128 output.png`**
#### Linux/OSX
**`convert input.jpg -filter point -monochrome -resize 1000x128 output.png`**
for grayscale instead replace the **`-monochrome`** flag with **`-colorspace Gray`**

### Running Python script
Make sure the output.png image is in the folder of the main python script. 
To run the script in terminal or powershell type 
**`python3 ./trial.py`** (for black and white aka -monochrome)
-or- 
**`python3 ./trial_gs.py`** (for grayscale)

Grayscale filter w/trial_gs.py will output the midi where the color level controls the note velocity

#### Notes:
- trial.py will merge consecutive notes

