# Importing the Image module from the PIL (Pillow) library to work with images
from PIL import Image
# Importing the os module to interact with the operating system
import os

# Get the current working directory
myPath = os.getcwd()

# Check if the current directory name includes 'PicturToPdf'
if 'PicturToPdf' in myPath:
    newPath = myPath  # If yes, use it as the working directory
else:
    # If not, append 'PicturToPdf' to the current path
    newPath = myPath + '\\' + 'PicturToPdf'

# Change the current working directory to newPath
os.chdir(newPath)

# Print the current working directory
print(os.getcwd())

# Print the list of files and directories in the newPath
print('Files and Directories:')
print(os.listdir(newPath))

# Ask the user to enter the name of the picture file they want to convert
print("Enter Name of PictureFile you want to convert to a Pdf")
picturToPdf = input()  # Accept user input (e.g., 'image.jpg')

# Open the image file using PIL
image1 = Image.open('{}'.format(picturToPdf))

# Convert the image to RGB mode (required for saving as PDF)
im1 = image1.convert('RGB')

# Save the image as a PDF with the same name as the input image
im1.save('{}.pdf'.format(picturToPdf))

# Notify the user that the process is finished
print('Finished')
