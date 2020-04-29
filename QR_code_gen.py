#S1:-
#pip install pyqrcode
#pip install pypng
#s2
import pyqrcode
name = 'spidy'
k = pyqrcode.create(name)
k.png(name+'.png',scale=10)
#To open Image automatically
import os
os.system(name+'.png')