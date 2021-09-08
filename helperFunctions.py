from sklearn.model_selection import train_test_split
import pandas as pd
from imageDownloader import DEGREE
import random
import numpy as np
from PIL import Image, ImageOps

'''Function to find the north-west boundary of the image using central co-ordinates'''


def nw_lat_long_manip(lat, long):
    # ans = ((lat + 0.002750) * DEGREE, (long - 0.001700) * DEGREE)     # Rectangular Dimensions
    ans = ((lat + 0.00222223) * DEGREE, (long - 0.0025) * DEGREE)  # Square Dimensions
    return ans


'''Function to find the south-east boundary of the image using central co-ordinates'''


def se_lat_long_manip(lat, long):
    # ans = ((lat - 0.002700) * DEGREE, (long + 0.001700) * DEGREE)  # Rectangular Dimensions
    ans = ((lat - 0.00194444) * DEGREE, (long + 0.0025) * DEGREE)  # Square Dimensions
    return ans


'''Function to find random co-ordinates to generate test satellite images'''


def random_co_ordinate_generator(a_list, b_list):
    latitude = 0
    longitude = 0
    dice = random.randint(1, 4)
    # if latitude in a_list or longitude in b_list:  Not Necessary to check
    #     random_co_ordinate_generator(a_list, b_list)
    if dice == 1:
        # Northern California
        latitude = random.uniform(38.99, 41.984)
        longitude = random.uniform(-123.78, -120.001)
    elif dice == 2:
        # Left half or Central California
        latitude = random.uniform(34.44, 38.90)
        longitude = random.uniform(-121.45, -119.84)
    elif dice == 3:
        # Central California
        latitude = random.uniform(34.58, 36.63)
        longitude = random.uniform(-120.68, -116.66)
    elif dice == 4:
        # Southern California
        latitude = random.uniform(32.73, 34.48)
        longitude = random.uniform(-117.44, -114.80)

    if ((latitude - 0.00222223) or (latitude + 0.00222223)) in a_list \
            or ((longitude + 0.0025) or (longitude - 0.0025)) in b_list:
        random_co_ordinate_generator(a_list, b_list)

    return latitude, longitude


'''---------------Functions for the ML Algorithm--------------------'''

directory = r'C:\ML Research Materials\Image Set'

"""
Function to load and divide the dataset into training and testing portions
Enter variables in the format: (training_data, training_labels), (testing_data, testing_labels)
Change the np.array size everytime the dataset changes
"""


def load_data():

    # Creating the initial pathways and datasets
    image_set = np.zeros((5000, 400, 400))
    image_type = np.zeros(5000)
    resize = (400, 400)
    df = pd.read_csv('dairyFarmLocations.csv', usecols=['VistaSType'])
    location_type = df.get('VistaSType')

    # A loop for the dairy locations
    for i in range(1715):

        # Accessing and correcting the picture
        filename = f'{i}.png'
        picture = Image.open(directory + "\\" + filename)
        picture = picture.resize(resize)
        picture = picture.convert('1')  # Converts the image to B/W
        # picture = ImageOps.grayscale(picture)  #Converts image to Grayscale instead of B/W

        # Passing it into the NumPy array containing the whole set
        image_set[i, :, :] = np.array(picture)[:, :]
        if location_type[i] == 'Dairy':
            image_type[i] = 1

    # A loop for the non-dairy locations
    for j in range(1715, 5000):
        # Accessing and correcting the picture
        filename = f'{j}.png'
        picture = Image.open(directory + "\\" + filename)
        picture = picture.resize(resize)
        picture = picture.convert('1')
        # picture = ImageOps.grayscale(picture)  #Converts image to Grayscale instead of B/W
        # Passing it into the NumPy array containing the whole set

        '''The line below has to be updated every time the 1st Loop range changes'''
        size_correction = j - 0  # to offset the continuation in the np.array + fix out of bounds
        image_set[size_correction, :, :] = np.array(picture)[:, :]
        if location_type[j] == 'Dairy':
            image_type[size_correction] = 1

    # Splitting the train and test modules using the scikit learn package

    training_data, testing_data, training_labels, testing_labels = \
        train_test_split(image_set, image_type, test_size=0.2, random_state=42, shuffle=True)
    # Changed from image_type to image_type

    return (training_data, training_labels), (testing_data, testing_labels)

# RGB values of an 'Image not available' picture is [228 226 222]
