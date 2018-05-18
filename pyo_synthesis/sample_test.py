from pyo import *

s = Server().boot()
s.start()
sf = SfMarkerLooper("sample.aif", speed=[.999,1], mul=.3).out()
s.gui(locals())
