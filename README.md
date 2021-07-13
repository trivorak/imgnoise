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