import pyperclip #Library for Copying things
import os #The Library for manuevering in the File systems
import tkinter #Library for app dev
from tkinter import ttk
from tkinter import *


# The Path of the file for the gcode file
file_path = r"C:\Users\morei\OneDrive\Documents\GitHub\CPT-101\Gcode Automation Script\3DBenchy_PLA_37m39s.gcode"
# Amount of Copies of the Gcode
copies = 2
# Output of the Operation:
# output_path = r"C:\Users\morei\OneDrive\Documents\GitHub\CPT-101\Gcode Automation Script\Outputs" #Old Output path

# Do the thing
try:
    # The Paths for the new file with the copies
    folder_path = os.path.dirname(file_path)
    output_path = os.path.join(folder_path, f"{file_path}_QTY_{copies}.gcode")


    # opens the soruce file and reads it 
    with open(file_path, "r", encoding="utf-8") as file:
        #creates a variable with the contents of the file
        contents = file.read()
    
    # Writes the number of copies of the gcode file:
    with open(output_path, "w", encoding="utf-8") as out_file:
        for i in range(copies):
            out_file.write(contents) #Writes the amount of copies of the gcode into 1 file
            out_file.write("\n") #Adds a blank line at the end of the file
            print(f"wrote {i+1} of {copies}")

    print(f"Saved to {output_path}")
    
# When it breaks
except FileNotFoundError:
    print("can't find it")
except Exception as e:
    print(f"it broke because {e}")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)
root.mainloop()