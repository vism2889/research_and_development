# synthesis using pyo library during residency at R&D

'''
To execute use: 'pythonw filename.py' at the command line instead of 'python filename.py'.
Will look into this problem more in the future.
'''

'''
weird FM synth with pyo as an initial go about!
TODO:
- Implement midi + midi-learn
- Implement better paramter control
- Implement Audio in from .wav file


'''

from pyo import *

s = Server().boot()
s.amp = 0.1

sd = SineLoop(freq=100, mul=0.1,feedback=0.3)
a = FM()
a.ctrl()
b = CrossFM()
b.ctrl()
c = sd
c.ctrl()
fm1 = FM(carrier=(a*c)+(a/b), ratio=[1.5,1.49], index=10, mul=0.3)
fm1.ctrl()
fm2 = CrossFM(carrier=fm1+a+b+c, ratio=[1.5,1.49], ind1=10, ind2=2, mul=0.3)
fm2.ctrl()

#
sel = Selector([fm1+fm2, fm2, a, b, c]).out()
sel.ctrl(title="Input interpolator (0=FM, 1=CrossFM, 2=FM, 3=CrossFM, 4=SineLoop)")
sel2 = Selector([sel, fm2, a, b, c]).out()
sel2.ctrl(title="Input interpolator (0=FM, 1=CrossFM, 2=FM, 3=CrossFM, 4=SineLoop)")



s.gui(locals())
