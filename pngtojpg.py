# Import the Image class from the Pillow library to handle image operations
from PIL import Image
# Import the os module to interact with the file system
import os

# Get the current working directory
myPath = os.getcwd()

# Check if the directory name includes 'PNGtoJPG'
if 'PNGtoJPG' in myPath:
    newPath = myPath  # If yes, use it as is
else:
    # If not, append 'PNGtoJPG' to the current path to form the new path
    newPath = myPath + '\\' + 'PNGtoJPG'

# Change the current working directory to the target directory
os.chdir(newPath)

# Print the current working directory to confirm the path change
print(os.getcwd())

# List and print all files and directories in the new working directory
print('Files and Directories:')
print(os.listdir(newPath))

# Prompt the user to enter the name of the image file to convert
print("Enter Name of PictureFile you want to convert to a jpg")
imageName = input()  # e.g., 'image.png'

# Open the specified image file for reading
savedImage = Image.open(imageName, mode='r', formats=None)

# Save the opened image as a new JPG file named '01.jpg'
savedImage.save('01.jpg')

# Notify the user that the process is complete
print('Finished')
