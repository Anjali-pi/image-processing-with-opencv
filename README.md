penCV Image Processing Basics
1- Overview
This repository contains a beginner-level  demonstrating fundamental image processing techniques using Python and OpenCV. it  applies various transformations on a single image to understand core concepts of computer vision.

2- Features / Operations
This project performs the following operations:

 Load and display image
 Brightness adjustment
 Convert image to grayscale
 Resize image
 Crop region of interest
 Rotate image (45 degrees)
 Apply Gaussian blur
 Edge detection using Canny Draw rectangle and add label
 Add custom text on image
 
## Technologies Used
Python 
OpenCV (cv2)

##Input Image
mountain.jpg (sample input image used for processing)
##Output Images Generated

After running the script, the following outputs are created:
output.jpg → Brightness adjusted image
gray.jpg → Grayscale image
resized.jpg → Resized image
cropped.jpg → Cropped section
rotated.jpg → Rotated image
blurred.jpg → Blurred image
edges.jpg → Edge detection result
annotated.jpg → Image with rectangle and text
text.jpg → Image with custom text

## How to Run
Using Jupyter Notebook
Install OpenCV (run this in a notebook cell):
!pip install opencv-python
Open the notebook file:
Open the .ipynb file in Jupyter Notebook or VS Code
Run all cells step by step to see outputs.

#If using VS Code Notebook
Open .ipynb file
Click Run All

# Important Note
Since OpenCV uses image windows (cv2.imshow()), in notebooks:
Sometimes cv2.imshow() may not work properly
You can use matplotlib instead if needed

📚 What I Learned
Basics of OpenCV library
Image transformations and filtering
Edge detection techniques
Drawing shapes and text on images
Working with pixel-level image manipulation

👩‍💻 Author
Anjali Singh Yadav

# Note

This is a beginner-friendly computer vision project created for learning and practice purposes.

