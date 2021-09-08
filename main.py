import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageOps
import imageDownloader
import helperFunctions
import pandas as pd
from PIL import Image
import csv

'''####################################--MAIN CALL--####################################'''
col_list = ['Latitude', 'Longitude', 'VistaSType']
# Accessing the dairy farm Locations coordinates in the CSV file
df = pd.read_csv('dairyFarmLocations.csv', usecols=col_list)

directory = r'C:\ML Research Materials\Image Set'

# if __name__ == '__main__':  # Enter the coordinates for the cattle farm in the functions below.
#     for i in range(1715):
#         NW_lat_long = helperFunctions.nw_lat_long_manip(df.loc[i].at["Latitude"],
#                                                         df.loc[i].at["Longitude"])
#         SE_lat_long = helperFunctions.se_lat_long_manip(df.loc[i].at["Latitude"],
#                                                         df.loc[i].at["Longitude"])
#
#         # Higher the zoom increases, longer it takes
#         # It also uses more number of calls per image accordingly
#
#         result = imageDownloader.get_maps_image(NW_lat_long, SE_lat_long, zoom=18)
#         filename = f'{i}.png'
#         result.save(directory + '\\' + filename, 'PNG')
# #         result.show()

# with open('dairyFarmLocations.csv', mode='a', newline='') as csv_file:
#     fieldnames = ['', 'X', 'Y', 'Name', 'description', 'altitudeMode', 'City', 'VistaIPCC', 'Vista_ID',
#                   'VistaDate', 'Longitude', 'Source', 'State', 'FID', 'Latitude', 'VistaName', 'VistaSType', 'Field_1']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # writer.writeheader()

    # for j in range(1715, 5000):
    #     random_co_ordinate = \
    #         helperFunctions.random_co_ordinate_generator(df['Latitude'], df['Longitude'])
    #     latitude, longitude = random_co_ordinate
    #     NW_lat_long = helperFunctions.nw_lat_long_manip(latitude, longitude)
    #     SE_lat_long = helperFunctions.se_lat_long_manip(latitude, longitude)
    #
    #     result = imageDownloader.get_maps_image(NW_lat_long, SE_lat_long, zoom=18)
    #
    #     writer.writerow({'': j, 'Longitude': longitude, 'Latitude': latitude,
    #                      'VistaSType': 'Non-Dairy'})
    #
    #     filename = f'{j}.png'
    #     result.save(directory + '\\' + filename, 'PNG')
    #     # result.show()


