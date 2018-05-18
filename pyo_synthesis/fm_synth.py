from pyo import *
POLY = 10

class synth:
    def __init__(self):
        self.note = Notein(poly=POLY, scale=0)
        self.port = Port(self.note['velocity'], .001, .5)
        self.amp = Port(self.note["velocity"], risetime=.001, falltime=1)



class FMsynth(synth):
    def __init__(self):
        synth.__init__(self)
        self.sin1 = Sine(freq=self.note['pitch'], mul=self.amp*0.1)
        self.sin2 = Sine(freq=self.note['pitch'] * self.sin1, mul=self.amp*0.1)
        self.sin3 = Sine(freq=self.note['pitch'] * 1.005* self.sin2, mul=self.amp*0.1)
        self.sin = Sine(freq=self.note['pitch'], mul=self.amp*0.1)
        self.lfo = Sine([.31,.34], mul=15, add=20)
        self.crossfm = CrossFM(carrier=self.note['pitch'] * 1.005 * self.lfo, ratio=[.2499*self.sin,.2502], ind1=self.note['pitch'], ind2=self.sin, mul=self.amp*0.1)
        self.mix = Mix([self.crossfm.mix(), self.sin.mix(), self.sin1.mix(), self.sin2.mix()], voices=2).out()

s = Server().boot()
s.start()
fm = FMsynth()
s.gui(locals())
