import numpy as np

class Jacobian_Henon:
    def __init__(self, a=1.4, b=0.3):
        self.a, self.b = a, b
        
    
    def __call__(self, x):
        J = [[-2*x[0], self.b], [1, 0]]
        return J