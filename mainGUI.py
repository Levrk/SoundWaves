import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess

activeWaves = [False, False, False, False]

def submit():
    """
    Calls main.py with arguments gathered from any active waves
    """
    args = [str(waveType1.get()), str(amplitude1.get()), str(frequency1.get())]
    if (activeWaves[0] == True):
        args += [str(operator1.get()),str(waveType2.get()), str(amplitude2.get()), str(frequency2.get())]
    if (activeWaves[1] == True):
        args += [str(operator2.get()),str(waveType3.get()), str(amplitude3.get()), str(frequency3.get())]
    if (activeWaves[2] == True):
        args += [str(operator3.get()),str(waveType4.get()), str(amplitude4.get()), str(frequency4.get())]
    if (activeWaves[3] == True):
        args += [str(operator4.get()),str(waveType5.get()), str(amplitude5.get()), str(frequency5.get())]
    subprocess.run(["python3", "Backend/main.py"] + args)
    

def toggle1():
    #Toggle function for additional wave #1
    if activeWaves[0] == True:
        #Toggle off the first additional wave
        amplitude2.grid_remove()
        frequency2.grid_remove()
        waveType2.grid_remove()
        operator1.grid_remove()
        aLabel2.grid_remove()
        fLabel2.grid_remove()
        wLabel2.grid_remove()
        activeWaves[0] = False
    else:
        #Toggle on the first additional wave
        amplitude2.grid(row=2,column=4)
        operator1.grid(row=2,column=0,sticky="s")
        aLabel2.grid(row=2,column=3,sticky="s")
        fLabel2.grid(row=2,column=5,sticky="s")
        waveType2.grid(row=2,column=2,sticky="s")
        wLabel2.grid(row=2,column=1,sticky="s")
        frequency2.grid(row=2,column=6)
        toggle2.grid(row=3,column=7,sticky="s")
        toggle1.grid_remove()
        activeWaves[0] = True

def toggle2():
    #Toggle function for additional wave #2
    if activeWaves[1] == True:
        #Toggle off the second additional wave
        amplitude3.grid_remove()
        frequency3.grid_remove()
        waveType3.grid_remove()
        operator2.grid_remove()
        aLabel3.grid_remove()
        fLabel3.grid_remove()
        wLabel3.grid_remove()
        toggle2.grid_remove()
        toggle1.grid(row=2,column=7,sticky="s")
        activeWaves[1] = False
    else:
        #Toggle on the second additional wave
        amplitude3.grid(row=3,column=4)
        operator2.grid(row=3,column=0,sticky="s")
        aLabel3.grid(row=3,column=3,sticky="s")
        fLabel3.grid(row=3,column=5,sticky="s")
        waveType3.grid(row=3,column=2,sticky="s")
        wLabel3.grid(row=3,column=1,sticky="s")
        frequency3.grid(row=3,column=6)
        toggle3.grid(row=4,column=7,sticky="s")
        toggle2.grid_remove()
        activeWaves[1] = True

def toggle3():
    #Toggle function for additional wave #3
    if activeWaves[2] == True:
        #Toggle off the third additional wave
        amplitude4.grid_remove()
        frequency4.grid_remove()
        waveType4.grid_remove()
        operator3.grid_remove()
        aLabel4.grid_remove()
        fLabel4.grid_remove()
        wLabel4.grid_remove()
        toggle3.grid_remove()
        toggle2.grid(row=3,column=7,sticky="s")
        activeWaves[2] = False
    else:
         #Toggle on the third additional wave
        amplitude4.grid(row=4,column=4)
        operator3.grid(row=4,column=0,sticky="s")
        aLabel4.grid(row=4,column=3,sticky="s")
        fLabel4.grid(row=4,column=5,sticky="s")
        waveType4.grid(row=4,column=2,sticky="s")
        wLabel4.grid(row=4,column=1,sticky="s")
        frequency4.grid(row=4,column=6)
        toggle4.grid(row=5,column=7,sticky="s")
        toggle3.grid_remove()
        activeWaves[2] = True

def toggle4():
    #Toggle function for additional wave #4
    if activeWaves[3] == True:
         #Toggle off the fourth additional wave
        amplitude5.grid_remove()
        frequency5.grid_remove()
        waveType5.grid_remove()
        operator4.grid_remove()
        aLabel5.grid_remove()
        fLabel5.grid_remove()
        wLabel5.grid_remove()
        toggle3.grid(row=4,column=7,sticky="s")
        toggle4.grid_remove()
        activeWaves[3] = False
    else:
         #Toggle on the fourth additional wave
        amplitude5.grid(row=5,column=4)
        operator4.grid(row=5,column=0,sticky="s")
        aLabel5.grid(row=5,column=3,sticky="s")
        fLabel5.grid(row=5,column=5,sticky="s")
        waveType5.grid(row=5,column=2,sticky="s")
        wLabel5.grid(row=5,column=1,sticky="s")
        frequency5.grid(row=5,column=6)
        activeWaves[3] = True

#initializing tkinter
root = tk.Tk()
root.title("Sound Wave Visualizer")
root.geometry("800x500")
frame = tk.Frame(root, bd=2,padx=10, pady=10)


# first wave
amplitude1 = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal")
aLabel1 = tk.Label(root,text=" Amplitude: ")
aLabel1.grid(row=1,column=3,sticky="s")
amplitude1.grid(row=1,column=4)

frequency1 = tk.Scale(root, from_=20, to=15000, resolution=100, orient="horizontal")
frequency1.grid(row=1,column=6)
fLabel1 = tk.Label(root,text=" Frequency(hz): ")
fLabel1.grid(row=1,column=5,sticky="s")

wLabel1 = tk.Label(root,text=" Wave Type: ")
waveType1 = ttk.Combobox(root, values=["Sine", "Square", "Sawtooth", "Triangle", "Noise"],state="readonly")
waveType1.current(0)
waveType1.grid(row=1,column=2,sticky="s")
wLabel1.grid(row=1,column=1,sticky="s")


#second wave
operator1var = tk.IntVar()
operator1 = ttk.Combobox(root, values=["Multiply", "Add"],state="readonly", width=7)
operator1.current(0)

amplitude2 = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal")
aLabel2 = tk.Label(root,text=" Amplitude: ")

frequency2 = tk.Scale(root, from_=20, to=15000, resolution=100, orient="horizontal")
fLabel2 = tk.Label(root,text=" Frequency(hz): ")

wLabel2 = tk.Label(root,text=" Wave Type: ")
waveType2 = ttk.Combobox(root, values=["Sine", "Square", "Sawtooth", "Triangle", "Noise"],state="readonly")
waveType2.current(0)

#toggles the first additional wave
toggle1 = tk.Button(root, text="+/-", command=toggle1)
toggle1.grid(row=2,column=7,sticky="s")

#third wave
operator2var = tk.IntVar()
operator2 = ttk.Combobox(root, values=["Multiply", "Add"],state="readonly", width=7)
operator2.current(0)

amplitude3 = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal")
aLabel3 = tk.Label(root,text=" Amplitude: ")

frequency3 = tk.Scale(root, from_=20, to=15000, resolution=100, orient="horizontal")
fLabel3 = tk.Label(root,text=" Frequency(hz): ")

wLabel3 = tk.Label(root,text=" Wave Type: ")
waveType3 = ttk.Combobox(root, values=["Sine", "Square", "Sawtooth", "Triangle", "Noise"],state="readonly")
waveType3.current(0)

#toggles the second additional wave
toggle2 = tk.Button(root, text="+/-", command=toggle2)

#fourth wave
operator3var = tk.IntVar()
operator3 = ttk.Combobox(root, values=["Multiply", "Add"],state="readonly", width=7)
operator3.current(0)

amplitude4 = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal")
aLabel4 = tk.Label(root,text=" Amplitude: ")

frequency4 = tk.Scale(root, from_=20, to=15000, resolution=100, orient="horizontal")
fLabel4 = tk.Label(root,text=" Frequency(hz): ")

wLabel4 = tk.Label(root,text=" Wave Type: ")
waveType4 = ttk.Combobox(root, values=["Sine", "Square", "Sawtooth", "Triangle", "Noise"],state="readonly")
waveType4.current(0)

#toggles the third additional wave
toggle3 = tk.Button(root, text="+/-", command=toggle3)

#fifth wave
operator4var = tk.IntVar()
operator4 = ttk.Combobox(root, values=["Multiply", "Add"],state="readonly", width=7)
operator4.current(0)

amplitude5 = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal")
aLabel5 = tk.Label(root,text=" Amplitude: ")

frequency5 = tk.Scale(root, from_=20, to=15000, resolution=100, orient="horizontal")
fLabel5 = tk.Label(root,text=" Frequency(hz): ")

wLabel5 = tk.Label(root,text=" Wave Type: ")
waveType5 = ttk.Combobox(root, values=["Sine", "Square", "Sawtooth", "Triangle", "Noise"],state="readonly")
waveType5.current(0)

#toggles the fourth additional wave
toggle4 = tk.Button(root, text="+/-", command=toggle4)



#submit button

submit_button = Button(root, text="Visualize", command=submit)
submit_button.grid(row=9, column=4)

# This will create an empty window with the title "Empty Page"
root.mainloop()