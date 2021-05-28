##Contains Python functions for HW08, BDS 311
##These functions will be generated collaboratively and called in each user's separate Jupyter notebook

#import standard packages here

import numpy as np


def make_standard_units(input_array):
    '''Converts input_array to standard_units, where data has mean 0 and standard deviation of 1
        INPUT: data array
        OUTPUT: array in standard units'''
    #Content in this function is exactly the way I did mine, looks good -Sophie
    
    sub_arr = input_array - np.mean(input_array)
    std_arr = sub_arr / np.std(input_array)
    return std_arr

    
def calc_corrcoef_from_standardized_input(array1,array2):
    '''Calculates Pearson correlation coefficient from two arrays in standard units
    INPUT: array1, array2: In standard units
    OUTPUT: Pearson correlation coefficient'''
    #I wrote this function the same way we did in class, using np.mean, but this looks good -Sophie
    
    coefs = np.corrcoef(array1, array2)
    return coefs[0][1]

def get_regression_parameters(array1, array2):
    '''Calculates regression parameteres from two input arrays
    INPUT: array1, array2: two data arrays
    OUTPUT: regression_array, length 2: regression_array[0] is slope and regression_array[1] is intercept'''
    # Function looks great -Alex
    
    arr1_norm = make_standard_units(array1)
    arr2_norm = make_standard_units(array2)
    coef = calc_corrcoef_from_standardized_input(arr1_norm, arr2_norm)
    
    xstd = np.std(array1)
    ystd = np.std(array2)
    m = coef * (ystd / xstd)
    
    xmean = np.mean(array1)
    ymean = np.mean(array2)
    b = ymean - m * xmean
    
    return [m, b]
    



