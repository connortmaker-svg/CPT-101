import pyperclip #Library for 
import os #The Library for manuevering in the File systems

# The Path of the file for the gcode file
file_path = r"C:\Users\morei\OneDrive\Documents\GitHub\CPT-101\Gcode Automation Script\3DBenchy_PLA_37m39s.gcode"
# Amount of Copies of the Gcode
copies = 2

# Do the thing
try:
    # opens the file and reads it 
    with open(file_path, "r", encoding="utf-8") as file:
        #creates a variable with the contents of the file
        contents = file.read()
        #using the pyerpclip library, it performs a copy function
        pyperclip.copy(contents)
        print("File has been copied")

# When it breaks
except FileNotFoundError:
    print("can't find it")
except Exception as e:
    print("it broke because {e}")