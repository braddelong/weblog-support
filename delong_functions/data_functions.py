import pandas_datareader
from pandas import DataFrame, Series
import pandas as pd
import os
from urllib.request import urlretrieve

def getdata_read_or_download(filename, source_URL, force_download = False):
    '''Use pandas to read in data from a specified local file in the current
    working directory, or download data from a specified source URL if the 
    local file does not exist in the current working directory. Download
    can be forced if the local file is corrupt or simply needs to be updated.
    
    Parameters:
    ===========
    filename : string                  # location of already-dowloaded data in current working directory
    source_URL : string                # location of data on internet
    force_download: boolean (optional) # if True, force redownload of data
        
    Returns:
    ========
    datafame : pandas dataframe        # the data file for the analysis'''
    
    if ((force_download == True) or not os.path.exists(filename)):
        urlretrieve(source_URL,filename)
    dataframe = pd.read_csv(filename)
    return dataframe

    # Use: from delong_functions.data_functions import getdata_read_or_download # get or download data file

# ----
#
# These are statistics functions for Brad DeLong's jupyter notebooks. Should exist 
# in two copies, one each inside the delong_functions directories of Brad DeLong's
# private jupyter notebook backup github repository and of Brad DeLong's public
# weblog-support github repository.
#
# Use: from delong_functions.stat_functions import *


