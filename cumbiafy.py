# Cumbiafy.py - Give a cumbia feeling to any song.
# Author: Miguel Cabrera <mfcabrera@gmail.com>

import os
import time
import argparse



import echonest.remix.audio as audio

# Make a song sounds like cumbia
# Originally planned for the Music Hacking even in Munich in Summer 2012 but
# my HD died that day. So no released. 
# I based my code on cowbel code of the Echonest remix samples.

soundsPath = "sounds/"
guacharaca_file =  "guacharaca.wav"
llamador_file = "llamador.wav"



guacharaca_sound = audio.AudioData(os.path.join(soundsPath,"%s" % guacharaca_file))
llamador_sound = audio.AudioData(os.path.join(soundsPath,"%s" % llamador_file))

GUACHARACA_OFFSET = -0.015



    # Helper function for dealing with volume
def linear(input, in1, in2, out1, out2):
    return ((input-in1) / (in2-in1)) * (out2-out1) + out1
    # Helper function for dealing with volume
def exp(input, in1, in2, out1, out2, coeff):
    if (input <= in1):
        return out1
    if (input >= in2):
        return out2
    return pow( ((input-in1) / (in2-in1)) , coeff ) * (out2-out1) + out1



class Cumbiafy:
    def __init__(self,input_file,guacharaca_intensity,llamador_intensity):
        self.audiofile = audio.LocalAudioFile(input_file)
        self.audiofile.data *= linear(self.audiofile.analysis.loudness, -2, -12, 0.5, 1.5) * 0.75
        self.llamador_intensity = llamador_intensity
        self.guacharaca_intensity = guacharaca_intensity
        

    def run(self,out,guacharaca_intensity=1,llamador_intencity=1):
        
        t1 = time.time()
        
        sequence = self.sequence(guacharaca_sound)
        
        print "Sequence and mixed in %g seconds"   % (time.time() - t1)

        self.audiofile.encode(out)

    def sequence(self,sound):
        llamador_volume = linear(self.llamador_intensity, 0, 1, 0.1, 0.3)
        guacharaca_volume = linear(self.guacharaca_intensity, 0, 1, 0.1, 0.3)
        for beat  in self.audiofile.analysis.beats:
            #mix the audio
            
            self.mix(beat.start+GUACHARACA_OFFSET, seg=guacharaca_sound,volume=guacharaca_volume)
            self.mix(beat.start + beat.duration/2+GUACHARACA_OFFSET, seg=llamador_sound,volume=llamador_volume)
            
    def mix(self, start=None, seg=None, volume=0.3, pan=0.):
        # this assumes that the audios have the same frequency/numchannels
        startsample = int(start * self.audiofile.sampleRate)
        seg = seg[0:]
        seg.data *= (volume-(pan*volume), volume+(pan*volume)) # pan + volume
        if self.audiofile.data.shape[0] - startsample > seg.data.shape[0]:
            self.audiofile.data[startsample:startsample+len(seg.data)] += seg.data[0:]        
    
def main(inputFilename,outputFilename,guacharaca_intensity,llamador_intensity):
    c = Cumbiafy(inputFilename,guacharaca_intensity,llamador_intensity)
    print "Volviendonos cumbiamberos...."
    c.run(outputFilename,guacharaca_intensity,llamador_intensity)


# The wrapper for the script.  
if __name__ == '__main__':
    import sys


    parser = argparse.ArgumentParser(description='Give  a cumbia feeling to any song.')
    
    
    parser.add_argument('-i','--input',required=True,
                        help='Input file to convert. MP3 or WAV.')
    
    parser.add_argument('-o','--output',required=True,
                        help='Output file name - an mp3')
    
    parser.add_argument('-l','--llamador-intensity', type=float,default=1.25,
                        help='Llamador intensity,  1.25 by default.')
    
    parser.add_argument('-g','--guacharaca-intensity', type=float,default=1.25,
                        help='The guacharaca intensisty, 1.25 by default.')
    
    
    args = parser.parse_args()



    try :
        # This gets the filenames to read from and write to, 
        # and sets how loud the cowbell and walken samples will be
        inputFilename = args.input
        outputFilename = args.output
        guacharaca_intensity = args.guacharaca_intensity
        llamador_intensity  =  args.llamador_intensity
    except :
        # If things go wrong, exit!
        print "Oh crap - something went wrong"
        sys.exit(-1)
    main(inputFilename, outputFilename,guacharaca_intensity,llamador_intensity)



















