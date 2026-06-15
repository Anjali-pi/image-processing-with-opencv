## Image Processing with OpenCV: A Computer Vision Learning Project

##About the Project

This repository contains a structured collection of OpenCV programs covering fundamental to intermediate computer vision concepts. It demonstrates image processing, filtering, transformations, color analysis, and video processing using Python.

The goal is to build strong foundational knowledge in Computer Vision through practical implementation.

## Repository Structure

image-processing with-opencv/

├── 01_images_read_and_write/

├── 02_image_filter/

├── 03_color_space_and_thresholding/

├── 04_blur_images_and_edges_detection/

├── 05_image_transformations/

├── 06_working_with_video_files/

└── README.md

## Topics Covered
1️. Image Read & Write
Loading images using OpenCV
Saving processed images
Basic image operations (brightness adjustment, cropping, resizing, rotation)

2️. Image Filtering
Kernel-based filtering
Horizontal, vertical, diagonal filters
Custom convolution operations using cv2.filter2D

3️. Color Space & Thresholding
RGB ↔ BGR conversion
HSV and LAB color spaces
Grayscale conversion
Image masking using cv2.inRange
Thresholding techniques for segmentation

4️. Blurring & Edge Detection
Average blur
Gaussian blur
Median blur
Sobel edge detection
Laplacian edge detection
Canny edge detection

5️. Image Transformations
Affine transformation
Perspective transformation
Rotation
Shearing
Translation

6️. Video Processing
Reading video files frame-by-frame
Writing processed video output
Real-time video display
Grayscale video conversion
Blur video processing
Edge detection in video
Threshold video processing
Contour detection in video
Frame resizing and annotation

## Technologies Used

1.Python

2.OpenCV (cv2)

3.NumPy

4.Matplotlib

5.Jupyter Notebook

## Input Files
 
Sample images (.jpg, .png)

Sample video (.mp4) used for processing (not uploaded due to GitHub size limits)

**Note on Video Files

Due to GitHub file size limitations (25MB), video files are not included in this repository.
Instead, only code implementations for video processing are provided.

## How to Run
Using Jupyter Notebook

Install OpenCV (run this in a notebook cell):

!pip install opencv-python

Open the notebook file:

Open the .ipynb file in Jupyter Notebook or VS Code

Run all cells step by step to see outputs.

## If using VS Code Notebook
Open .ipynb file

Click Run All

## Important Note
Since OpenCV uses image windows (cv2.imshow()), in notebooks:

Sometimes cv2.imshow() may not work properly
You can use matplotlib instead if needed

# Key Learning Outcomes
1.Understanding image representation in OpenCV

2.Applying filters and transformations

3.Working with different color spaces

4.Implementing edge detection and segmentation

5.Processing real-time video streams

6.Building foundational Computer Vision skills

## Applications of This Project

1.Image processing systems

2.Object detection pipelines

3.Surveillance systems

4.Autonomous systems (basic vision)

5.AI & Machine Learning preprocessing

## Author
Anjali Singh Yadav








