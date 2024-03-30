#import googletrans as gt
#print(dir(gt))
#gt.LANGUAGES
#import flask as fl
#print(dir(fl)) 

from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)



def demo(x):
    for i in range(5):
        print("i = {}, x = {}".format(i, x))
        x = x + 1

demo(0)



import matplotlib.pyplot as plt
plt.plot(range(10), 'o')