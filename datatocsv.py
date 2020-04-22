# Convert reviewed files into a big CSV file
# Make sure to set working directory

import pandas as pd
YOUR_DIRECTORY = '/content/drive/My Drive/Colab Notebooks/ATMS597/project5/'

files = sorted(glob.glob(YOUR_DIRECTORY+'project5_data/reviewed/*.dat'))
df = pd.DataFrame()
for file in files:
    df = df.append(pd.read_csv(file, index_col=0))

df.to_csv(YOUR_DIRECTORY+'data.csv')
