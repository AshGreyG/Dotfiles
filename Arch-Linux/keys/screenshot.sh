#! /bin/bash

timestamp=$(date +"%Y-%m-%d %H%M%S")
filename="Screenshot ${timestamp}.png"
slurp | grim -g - "$filename"
dest="/home/ashgrey/Pictures/Screenshot"
mv "./$filename" "$dest"
if [ -f "$dest/$filename" ]; then
    notify-send "Screenshot saved as $filename"
else
    notify-send "Screenshot canceled"
fi
