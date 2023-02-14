import sys
import subprocess
import substring
a=sys.argv[1]
b=a[:len(a)-4]+'.mp3'
subprocess.run(['ffmpeg', '-i',                # or subprocess.call (Python 3.4 or lower)
    a,
    b
])