
import sys
import tkinter as tk
from tkinter import ttk
import math
import numpy as np

inductanceLabel, numWrapsLabel = None, None


# Define 30 different functions to be executed when the user selects an option
def function1():
    print("1 AWG")
    display_result("Cable Diameter: 0.2893 Inches", "Max Current: 119 Amperes", "Area of Wire: 42.4 MM Squared",
                   "Resistance of Copper Wire: 0.1239 Ohms")


def function2():
    print("2 AWG")
    display_result("Cable Diameter: 0.2576 Inches", "Max Current: 94 Amperes", "Area of Wire: 33.6 MM Squared",
                   "Resistance of Copper Wire: 0.1563 Ohms")


def function3():
    print("3 AWG")
    display_result("Cable Diameter: 0.2043 Inches ", "Max Current: 60 Amperes", "Area of Wire: 8.37 MM Squared",
                   "Resistance of Copper Wire: 0.2485 Ohms")

def calculateWraps(gauge):
    diameter = 8008.135
    area = 69.420
    inductance = 12345
    current = 54321
    resistance = 101.01
    length = 1

    numberOfWraps = np.sqrt(inductance * ((18 * diameter) + (40 * length)) / (diameter**2))

    return diameter, area, current, resistance, inductance, numberOfWraps

def displayCoilProperties(gauge, material, gaugeList):

    """
    #lists of coil properties corresponding to the gauge
    #diameters = [0 for i in range(len(gaugeList))]
    #currents = [0 for i in range(len(gaugeList))]
    #areas = [0 for i in range(len(gaugeList))]
    #resistance = [0 for i in range(len(gaugeList))]


    temp = [0 for i in range(len(gaugeList))]

    #here is all of the data for the properties for each material for each gauge
    properties = {
        "Copper":
            {
                "diameter":   temp,
                "current":    temp,
                "area":       temp,
                "resistance": temp
            },
        "Gold":
            {
                "diameter":   temp,
                "current":    temp,
                "area":       temp,
                "resistance": temp
            },
        "Silver":
            {
                "diameter":   temp,
                "current":    temp,
                "area":       temp,
                "resistance": temp
            },
        "Aluminium":
            {
                "diameter":   temp,
                "current":    temp,
                "area":       temp,
                "resistance": temp
            }

    }




    #gets the index of the selected gauge in the list of gauge options
    ind = gaugeList.index(gauge)

    display_result("diameter: " + str(properties[material]["diameter"][ind]),
                   "current: " + str(properties[material]["current"][ind]),
                   "area: " + str(properties[material]["area"][ind]),
                   "resistance: " + str(properties[material]["resistance"][ind]))
    """

    d, i, a, r, H, N = calculateWraps(gauge)

    display_result("diameter: " + str(d),
                   "current: " + str(i),
                   "area: " + str(a),
                   "resistance: " + str(r))


    inductanceLabel.config(text="Inductance: " + str(H))
    inductanceLabel.pack()

    numWrapsLabel.config(text="Number of Wraps: " + (f"{N:.5f}"))
    numWrapsLabel.pack()








#the themes for the app
themes = {
    "darkula":
        {
            "bg":"#282a36",
            "inac":"#6272a4",
            "low":"#256d1b",
            "idle":"#44475a",
            "up":"#8be9fd",
            "hlb": "black",
            "fg":"#f8f8f2",
            "ifg": "#f8f8f2"
        },
    "forest":
        {
            "bg":"#424342",
            "inac":"#244f26",
            "low":"#256d1b",
            "idle":"#149911",
            "up":"#1EFC1E",
            "hlb": "black",
            "fg":"white",
            "ifg": "white"
        },
    "doll":
        {
            "bg":"#ff9fb2",
            "inac":"#fbdce2",
            "low":"#0acdff",
            "idle":"#60ab9a",
            "up":"#dedee0",
            "hlb": "black",
            "fg":"white",
            "ifg": "white"
        },
    "ghost":
        {
            "bg":"#4B636F",
            "inac":"#CACACA",
            "low":"#E1E1E1",
            "idle":"#4B636F",
            "up":"#FFEEEE",
            "hlb":"black",
            "fg":"yellow",
            "ifg": "yellow"
        },
    "boardwalk":
        {
            "bg":"#2e282a",
            "inac":"#cd5334",
            "low":"#17bebb",
            "idle":"#edb88b",
            "up":"#fad8d6",
            "hlb":"black",
            "fg":"white",
            "ifg":"black"
        },
    "marble":
        {
            "bg":"#F3F3F3",
            "inac":"#F1E4E4",
            "low":"#EFE9E9",
            "idle":"#F8F8F8",
            "up":"#FFFFFF",
            "hlb":"black",
            "fg":"black",
            "ifg":"black"
        }
}

theme = "marble"






# Create the main application window
root = tk.Tk()
root.configure(bg=themes[theme]["bg"])
root.title("Coil Optimizer")
root.geometry("400x500")  # Set the window size to 400x500


#transparent color
trnsp = "#4B636F"
root.wm_attributes('-transparent', True)




#create the list of wire gauge options excluding specific ones, also create the numeric value for calculation later
excludeGauge = [3, 5, 6, 7, 9, 11, 13, 14, 15, 17]
gaugesNumeric = [0.5] + [i for i in range(1, 33) if not i in excludeGauge]
gaugeOptions = ["1/2 AWG"] + [str(gaugesNumeric[i]) + " AWG" for i in range(1, len(gaugesNumeric))] # Label options as "drop menu", "2 AWG", ..., "30 AWG"

var = tk.StringVar(root)
var.set(gaugeOptions[0])

# Create a frame to hold the widgets
frame = tk.Frame(root, bg=themes[theme]["bg"])
frame.pack()

# Create the user input box
input1_label = tk.Label(frame, text="Enter or Select Gauge of Wire", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
input1_label.pack()

input1_entry = tk.Entry(frame)
input1_entry.pack()

#label for the gauge dropdown
gauge_label = tk.Label(frame, text="Select Coil Gauge", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
gauge_label.pack(side=tk.LEFT)



# Create the dropdown menu
dropdown = tk.OptionMenu(frame, var, *gaugeOptions)
dropdown.config(bg=themes[theme]["bg"], fg=themes[theme]["fg"], highlightbackground=themes[theme]["hlb"], highlightcolor=themes[theme]["up"])
dropdown.pack(side=tk.LEFT)



# Create two input sections for the user to enter values
input1_label = tk.Label(root, text="Enter Desired Coil Diameter", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
input1_label.pack()
input1_entry = tk.Entry(root)
input1_entry.pack()

input2_label = tk.Label(root, text="Enter or Select Coil Material Type", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
input2_label.pack()
input2_entry = tk.Entry(root)
input2_entry.pack()

coilLengthInputLabel = tk.Label(root, text="Enter Coil Length", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
coilLengthInputLabel.pack()
coilLengthEntry = tk.Entry(root)
coilLengthEntry.pack()



# Create the dropdown menu
options = ["Copper", "Gold", "Silver", "Aluminium"]  # Options for the dropdown menu
var_material = tk.StringVar(root)
var_material.set(options[0])



# Create a frame to hold the widgets
frame_material = tk.Frame(root, bg=themes[theme]["bg"])
frame_material.pack()
material_label = tk.Label(frame_material, text="Select Coil Material", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
material_label.pack(side=tk.LEFT)


# Create the dropdown menu
dropdown_material = tk.OptionMenu(frame_material, var_material, *options)
dropdown_material.config(bg=themes[theme]["bg"], fg=themes[theme]["fg"], highlightbackground=themes[theme]["hlb"])
dropdown_material.pack(side=tk.LEFT)

# Set the padding for the label and dropdown
frame_material.pack(pady=(10, 0))




# Define a function to display the results of the selected function
def display_result(diameter, current, area, resistance):
    result_label.config(text=f"{diameter}\n{current}\n{area}\n{resistance}", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    result_label.pack()


# Define a function to be called when the user selects an option from the dropdown
def execute_function(*args):
    selection = var.get()
    materialSelection = var_material.get()

    displayCoilProperties(selection, materialSelection, gaugeOptions)

    #if selection == "1 AWG":
    #    function1()
    #elif selection == "2 AWG":
    #    function2()
    #elif selection == "30 AWG":
    #    function3()
    #else:
    #    # Check if selection is in range 3-29
    #    try:
    #        i = int(selection.split()[0])
    #        if 3 <= i <= 29:
    #            eval(f"function{i}()")  # Execute the function corresponding to the selected option
    #    except:
    #        pass


# Associate the function with the dropdown menu
var.trace("w", execute_function)


# Create a button to execute the selected function
button = tk.Button(root, text="Execute", command=execute_function, bg=themes[theme]["idle"], fg=themes[theme]["ifg"])
button.pack()

# Create a label to display the result of the selected function
result_label = tk.Label(root, text="Gauge Characteristics Displayed Here", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
result_label.pack()


inductanceLabel = tk.Label(root, text="Inductance: ", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
inductanceLabel.pack()

numWrapsLabel = tk.Label(root, text="Number of Wraps: ", bg=themes[theme]["bg"], fg=themes[theme]["fg"])
numWrapsLabel.pack()


# Start the application
root.mainloop()
