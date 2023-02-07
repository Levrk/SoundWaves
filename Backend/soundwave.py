import matplotlib.pyplot as mp
import numpy as np
from matplotlib.animation import FuncAnimation


class soundwave():
    """
    A class to generate different types of sound waves as a tuple of x and y values
    """
    def __init__(self, amplitude, frequency, type):
        """
        Initialize the class with the amplitude, frequency, and type of wave
        
        Arguments:
            amplitude (float): amplitude of the wave
            frequency (float): frequency of the wave
            type (str): type of wave. Can be "Sine", "Square", "Sawtooth", "Triangle", or "Pulse"
        """
        self.a = amplitude
        self.f = frequency
        self.type = type 


    def generate_sine(self):
        """
        Generates a sine wave with the given amplitude and frequency
        Returns: tuple: x and y values of the sine wave
        """
        x = np.linspace(-1,1,500000)
        y = self.a * np.sin(2 * np.pi * self.f * x)
        return (x,y)
    
    def generate_square(self):
        """
        Generates a square wave with the given amplitude and frequency
        
        Returns:tuple: x and y values of the square wave
        """
        x = np.linspace(-1,1,500000)
        y = self.a * np.sign(np.sin(2 * np.pi * self.f * x))
        return (x,y)
    
    def generate_sawtooth(self):
        """
        Generates a sawtooth wave with the given amplitude and frequency
        
        Returns: tuple: x and y values of the sawtooth wave
        """
        x = np.linspace(-1,1,500000)
        y = self.a * ((x / (1/self.f)) - np.floor(x / (1/self.f)))
        return (x,y)

    def generate_triangle(self):
        """
        Generates a triangle wave with the given amplitude and frequency
        
        Returns: tuple: x and y values of the triangle wave
        """
        x = np.linspace(-1,1,500000)
        x = x + .5/self.f
        y = self.a * 2 * np.abs((x / (1/self.f)) - np.floor((x / (1/self.f)) + 0.5))
        return (x,y)
    
    def generate_noise(self):
        ##will implement
        x = np.linspace(-1,1,500000)
        ###
        y = [np.random.uniform(0,self.a) for i in x]
        return (x,y)
        

    def generate_linespace(self):
        """
        Generates a wave of the given type
        
        Returns: tuple: x and y values of the wave
            
        """
        if (self.type == "Sine"):
            return self.generate_sine()
        elif (self.type == "Square"):
            return self.generate_square()
        elif (self.type == "Sawtooth"):
            return self.generate_sawtooth()
        elif (self.type == "Triangle"):
            return self.generate_triangle()
        elif (self.type == "Noise"):
            return self.generate_noise()
        
    
        