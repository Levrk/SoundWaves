import sys
import numpy as np
from graph import graph
from soundwave import soundwave
from linespace import linespace


#num of args provided in CL
num_args = len(sys.argv)
#list of options for wave_types and operators
wave_options = ["Sine", "Square","Sawtooth","Triangle","Noise"]
op_options = ["Multiply", "Add"]

#checking initial wave args to ensure valid type
if (np.isnan(float(sys.argv[2])) or np.isnan(float(sys.argv[3]))):
        raise TypeError("Amplitude and Frequency must be floats")
if (not str(sys.argv[1]) in wave_options):
    raise TypeError("Invalid wave type. Please select from Sine, Square, Sawtooth, Triangle, or Noise")
if (None in sys.argv[1:5]):
        raise TypeError("Invalid number of arguments")

#parsing arguments to create the initial wave
wave_type = str(sys.argv[1])
amplitude = float(sys.argv[2])
frequency = float(sys.argv[3])
#creating intial wave and linespace
mainWave = soundwave(amplitude, frequency, wave_type)
main_linespace = linespace(mainWave.generate_linespace())
avg_freq = frequency

#iterating over CL arguments
for i in range(4, num_args, 4):
    #checking CL args to ensure proper number and type
    if (np.isnan(float(sys.argv[i+2])) or np.isnan(float(sys.argv[i+3]))):
        raise TypeError("Amplitude and Frequency must be floats")
    if (not str(sys.argv[i+1]) in wave_options):
        raise TypeError("Invalid wave type. Please select from Sine, Square, Sawtooth, Triangle, or Noise")
    if (not str(sys.argv[i]) in op_options):
        raise TypeError("Invalid operator type. Please select either \"Multiply\" or \"Add\"")
    if (None in sys.argv[i:i+4]):
        raise TypeError("Invalid number of arguments")

    #fenerate new waveform to be applied
    wave_type = str(sys.argv[i+1])
    amplitude = float(sys.argv[i+2])
    frequency = float(sys.argv[i+3])
    #trying to optimize the sizing of the final window in relation to the waves frequencies
    avg_freq = (avg_freq + frequency)/2
    new_soundwave = soundwave(amplitude, frequency, wave_type)
    new_linespace = linespace(new_soundwave.generate_linespace())

    #apply operator
    if (str(sys.argv[i]) == "Add"):
        main_linespace += new_linespace
    elif (str(sys.argv[i]) == "Multiply"):
        main_linespace *= new_linespace
    
    
#create and show graph (linespace, amplitude, frequency) 
g = graph(main_linespace, main_linespace.get_max() , avg_freq)
g.main()


