# Cumbia.fy - Give you music a little bit of Cumbia.

Author: Miguel Cabrera <mfcabrera@gmail.com>


Make a song sounds a bit more like Cumbia. 
Cumbia is a popular latin-america genre originated in northern Colombia. This script add the basic Cumbia rythm
to an existing song. 
It was originally planned as a small demo for a music Hacking event in Munich in Summer 2012.
However, my HD died that day, so I couln't show it.


I based my code on  [More Cowbel](http://example.com/)  code from the
[Echonest Remix](http://echonest.github.io/remix/)
[samples](http://echonest.github.io/remix/examples.html).

Requires [Echonest Remix](http://echonest.github.io/remix/) and Python.

## Usage


    Usage: cumbiafy.py [-h] -i INPUT -o OUTPUT [-l LLAMADOR_INTENSITY]
                   [-g GUACHARACA_INTENSITY]

    Give a cumbia feeling to any song.

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT, --input INPUT
                        Input file to convert. MP3 or WAV.
    -o OUTPUT, --output OUTPUT
                        Output file name - an mp3
    -l LLAMADOR_INTENSITY, --llamador-intensity LLAMADOR_INTENSITY
                        Llamador intensity, 1.25 by default.
    -g GUACHARACA_INTENSITY, --guacharaca-intensity GUACHARACA_INTENSITY
                        The guacharaca intensisty, 1.25 by default.

