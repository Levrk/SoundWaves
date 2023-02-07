
import matplotlib.pyplot as mp
import numpy as np

class graph():

    def __init__(self,linespace, amplitude, frequency):
        self.linespace = linespace #linespace object
        self.amplitude = amplitude #float
        self.period = 1/frequency #float

    

    def main(self):
        #creates wave visualization
        fig = mp.figure(facecolor="#e4f0f2",edgecolor= "BLACK") # create a new figure
        ax = mp.axes() # create a new axes in the figure
        ax.plot(self.linespace.x,self.linespace.y,color="#4caf50")
        ax.set
        yMin, yMax = min(self.linespace.y), max(self.linespace.y)
        ax.set_xlim(-self.period*3,self.period*3)
        ax.set_ylim(yMin - yMax * 1/2, yMax * 3/2)
        mp.show() # display the figure
