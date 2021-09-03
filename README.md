# Virtual Drawing Pad

***

In this project, we create a Virtual Drawing Pad which allows us to draw or write on a computer screen according to the movements of a stylus in front of the computer camera.

## Methodology

This Virtual Drawing Pad was constructed using the Image Processing tools in OpenCV.

### Object Tracking using HSV Colour Thresholding

* We take each frame captured by the computer camera.
* Converted it from BGR to HSV.
* Thresholded the HSV image for a range of red color.

### Reducing Noise 

* We reduced considerable amount of noise by using Morphological Transformations of Closing and Opening.
* Applied Gaussian Blur. 

### Finding the Centroid and Drawing its path

* Using Contour features, we obtain the coordinates of the centroid of the object.
* We draw a circle for each centroid and draw connecting lines between the centroids of two frames.
* We keep updating the centroid coordinates of each frame in an array.

## Results

The object was tracked and its path was drawn.
Hence, the Virtual Drawing Pad was successfully constructed.

## Link to view project

Click [here] (https://drive.google.com/file/d/1tglRFiVe8_JYRL1ZRvvLwIqzjc9aXocv/view?usp=sharing) to view the demonstration of a Virtual Drawing Pad.
