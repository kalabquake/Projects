import sys
from comtypes.client import CreateObject
engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib

sys.argv.append('CleanCode_ch5.txt')

#engine = CreateObject("SAPI.SpVoice")
#stream = CreateObject("SAPI.SpFileStream")
outfile = input("Enter output name: ")
if('.wav' not in outfile):
    outfile+=".wav"
stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream
theText=""
if(len(sys.argv)>1):
    with open(sys.argv[1]) as f:
        theText=f.read()
else:
    theText=input("Enter text: ")
engine.speak(theText)
stream.Close()
