import numpy as np
import math

class Integrator:
    def __init__(self, xMin, xMax, N):
        ################################
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
        self.deltaX = 1.0*(xMax - xMin)/(N-1)
        self.integrationResult = 0
        
            
    def integrate(self):       
        ##################################
        for step in range(0,self.N-1):
            x_i = self.xMin + step*self.deltaX
            
            funcValue = ((x_i*x_i)*math.exp(-1*x_i)*math.sin(x_i))*self.deltaX  
            
            self.integrationResult = self.integrationResult + funcValue
        
    def show(self):
        ##################################
        print(round(self.integrationResult,5))

        

examp = Integrator(1,3,200)
examp.integrate()
examp.show()