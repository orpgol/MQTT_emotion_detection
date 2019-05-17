#! bin/bash

for DIR in `ls .`
do

for file in ./$DIR/*.wav
do

	sox $file -n spectrogram -r -o ${file}.png

done 

done 
