# Fire-Detection-System
Fire Detection System using Image processing

The aim of the project is to early detection of fire apart from preventive measures to reduce the losses due to hazardous fire.

In this project, we have developed a method to detect fires in different scenarios using image processing. To begin with, based on the static and dynamic characteristics of fire, a large number of non-fire images in the video stream are filtered. 

In the process, for the fire images in the video stream, the suspected fire area in the image is extracted. Eliminate the influence of light sources, candles and other interference sources to reduce the interference of complex environments on fire detection. Then, the algorithm encodes the extracted region and inputs it into convolution network, which extracts the depth feature of the image and finally judges whether there is a fire in the image.
