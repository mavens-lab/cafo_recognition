# cafo_recognition

A short Description of all the files that are used to execute the Image Recognition Project

dairyFarmLocations: Contains the co-ordinates of Dairy as well as Non-Dairy farms 
used as a test case to run the model. The total number of pictures that can be retrived is 5000

imageDownloader: This script contains the code that helps in downloading images from 
Google's Static Maps API that retrieves Satellite Images for the following project.

machineLearningModel: This file contains the code that creates, initializes, and runs
the project's Machine Learning Model

helperFunctions: This file contains functions that help satisfy some of the input modifications
that are too large to be written directly into the workflows specified above. It also 
contains functions that help automate repated tasks

main: This file contains the code used to download the images using the imageDownloader
script. It collects both the Dairy Farm downloading script and the Non-Dairy Farm script
