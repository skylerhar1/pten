##Contains Python functions for HW08, BDS 311
##These functions will be generated collaboratively and called in each user's separate Jupyter notebook

#import standard packages here

import numpy as np
import pandas as pd

def make_standard_units(input_array):
    #Skyler was here
    #this is looking good so far
    #mpg was late to the party again
    
    in_mean = np.mean(input_array)
    in_std = np.std(input_array)
    rms_array = [x-in_mean for x in input_array]
    rms_array = rms_array/in_std
    '''Converts input_array to standard_units, where data has mean 0 and standard deviation of 1
        INPUT: data array
        OUTPUT: array in standard units'''
    mean_sub = input_array - np.mean(input_array)
    array = mean_sub/np.std(input_array)
    return array

    
def calc_corrcoef_from_standardized_input(array1,array2):
    '''Calculates Pearson correlation coefficient from two arrays in standard units
    INPUT: array1, array2: In standard units
    OUTPUT: Pearson correlation coefficient'''
    #Riely added to this part
    
    correlation = np.mean(array1*array2)
    return correlation

def get_regression_parameters(array1, array2):
    '''Calculates regression parameteres from two input arrays
    INPUT: array1, array2: two data arrays
    OUTPUT: regression_array, length 2: regression_array[0] is slope and regression_array[1] is intercept'''
    #riely tried to add but did not finish this part skyler did I think?
    
    array1_su = make_standard_units(array1)
    array2_su = make_standard_units(array2)
    correlation = calc_corrcoef_from_standardized_input(array1_su,array2_su)
    ystd = np.std(array2)
    xstd = np.std(array1)
    ymean = np.mean(array2)
    xmean = np.mean(array1)
    slope = correlation* (ystd/xstd)
    intercept=ymean- slope *xmean
    return [slope, intercept]
    



