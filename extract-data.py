# -----------------------------------------------------------
# Validate a domain based on the majestic million data set
#
# (C) 2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: BSD 2-Clause License
# SPDX-License-Identifier: BSD 2-Clause License
# -----------------------------------------------------------

import pandas as pd

# default values and definitions
# - data file 
datafile = "majestic_million.csv"

# - default number of datasets for output
numberOfDatasets = 100

# - define individual weights per tld as a data frame
#   * define columns for weight and tlds
weights = [1.0, 0.5, 0.2]
tlds = ["default", "com", "tk"]
#   * transform these into a Pandas Series
s1 = pd.Series(tlds)
s2 = pd.Series(weights)
#   * define column description with tld as 1st column, and weight as 2nd column
d = {'tld': s1, 'weight': s2}
#   * create a data frame from it
individualWeights = pd.DataFrame(d)

# read data file as comma-separated CSV
data = pd.read_csv(datafile, sep=",")

# determine the unique top level domains from the dataset
listOfTlds = data.TLD.unique()

# go though the list of tlds
for tld in listOfTlds:
    # select the corresponding subset per tld
    subData = data[data["TLD"] == tld]

#    print(subData.head(numberOfDatasets))

#    break
