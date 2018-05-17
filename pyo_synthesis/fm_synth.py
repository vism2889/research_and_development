from pyo import *

s = Server().boot()
s.start()
sf = SfMarkerLooper("/sample.wav", speed=[.999,1], mul=.3).out()
s.gui(locals())
