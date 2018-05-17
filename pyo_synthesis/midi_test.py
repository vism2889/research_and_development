# 05/16/2018
'''
To execute use: 'pythonw filename.py' at the command line instead of 'python filename.py'.
Will look into this problem more in the future.
'''

'''
Experiments with receiving and routing midi in.
'''

from pyo import *

s = Server().boot()
s.start()

# Note in declarations
notes = Notein(poly=10, scale=1, mul=.5)
p = Port(notes['velocity'], .001, .5)
b = Sine(freq=notes['pitch'], mul=p).out()
c = Sine(freq=notes['pitch'] * 0.997, mul=p).out()
d = Sine(freq=notes['pitch'] * 1.005* c, mul=p).out()
ross = Rossler(pitch=.003, stereo=True, mul=.2, add=.2)
lf = Sine([.31,.34], mul=15*ross, add=20)
lf2 = LFO(freq=notes['pitch']/4 , sharp=.7*ross, type=2, mul=.4, add=.4).out()
a = LFO(freq=notes['pitch']*0.125, sharp=lf2, type=7, mul=100, add=300)
lf3 = LFO(freq=notes['pitch']*0.5, sharp=a, type=7, mul=100, add=250)

s1 = Sine(freq=b*c, mul=p)
s2 = Sine(freq=s1, mul=p).out(1)

ind = LinTable([(0,.3), (20,.85), (300,.7), (1000,.5), (8191,.3)])
m = Metro(4).play()
tr = TrigEnv(m, table=ind, dur=4)
f2 = SumOsc(freq=[301,300]*notes['pitch'], ratio=[.2498,.2503], index=tr, mul=.2)
f = CrossFM(carrier=notes['pitch'] * 1.005 * lf3, ratio=[.2499*ross,.2502], ind1=b*notes['pitch'], ind2=c, mul=.2).out()
harm = Harmonizer(f, transpo=-5*notes['pitch'], winsize=0.05).out(1)
chor = Chorus(harm, depth=[1.5,1.6*notes['pitch']], feedback=0.5, bal=0.5).out(1)
d = WGVerb(chor*f2*f, feedback=[.74,.75], cutoff=5000*lf, bal=.25, mul=.3).out()
s.gui(locals())
# midi control
'''
s = Server().boot()
s.start()
m = Midictl(ctlnumber=[107,102], minscale=250, maxscale=1000)
p = Port(m, .02)
a = Sine(freq=p, mul=.3).out()
a1 = Sine(freq=p*1.25, mul=.3).out()
a2 = Sine(freq=p*1.5, mul=.3).out()
'''
