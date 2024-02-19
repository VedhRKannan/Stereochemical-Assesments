import pandas as pd

# read contents of csv file
file = pd.read_csv("example/2nn8_angles.tsv")
print("\nOriginal file:")
print(file)

# adding header
headerList = ['Chain', 'Phi', 'Psi', 'Residue']

# converting data frame to csv
file.to_csv("example/2nn8_angles.tsv", header=headerList, index=False)

# display modified csv file
file2 = pd.read_csv("example/2nn8_angles.tsv")
print('\nModified file:')
print(file2)
