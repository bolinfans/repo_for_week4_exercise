import numpy as np
import pandas as pd

# In this file, you'll put all the functions for loading data.

pd.read_csv(Skyserver_starf.csv)


#-------------------------------------------------
# Ayush's needlessly convoluted load function

# Importing required modules
import numpy as np

# Loading .csv file (note for objects without a redshift value, it is set to 0)
def readfile(filename: str):
    obj_id, ra, dec, u, g, r, i, z = np.genfromtxt(filename, skip_header=2, delimiter = ',', usecols=(0, 1, 2, 3, 4, 5, 6, 7), unpack=True)
    redshift = np.genfromtxt(filename, skip_header=2, delimiter = ',', usecols=8, unpack=True, filling_values=0.0)
    obj_class = np.genfromtxt(filename, skip_header=2, delimiter = ',', usecols=9, unpack=True, dtype='str')
    
    return obj_id, ra, dec, u, g, r, i, z, redshift, obj_class
#-------------------------------------------------

pd.read_csv('../data_SDSS.csv')

print('Data Loaded!)

