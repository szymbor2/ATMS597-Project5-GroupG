# Convert reviewed files into a big CSV file
# Make sure to set working directory
import pandas as pd
from datetime import datetime

YOUR_DIRECTORY = '/content/drive/My Drive/Colab Notebooks/ATMS597/project5/'

# Grab all files that have been reviewed (parsed) and make a large dataframe
files = sorted(glob.glob(YOUR_DIRECTORY + 'project5_data/reviewed/*.dat'))
df = pd.DataFrame()
for file in files:
    df = df.append(pd.read_csv(file, index_col=0))

# Fix temperatures and dewpoint temperatures that are mixed around
for i in range(len(df)):
    if df['Temperature'].iloc[i] > df['Dewpoint'].iloc[i] or df['Temperature'].iloc[i] == df['Dewpoint'].iloc[i]:
        continue
    else:
        temp = copy.deepcopy(df['Temperature'].iloc[i])
        df['Temperature'].iloc[i] = copy.deepcopy(df['Dewpoint'].iloc[i])
        df['Dewpoint'].iloc[i] = temp
        
# Add another column to determine precip type (np.nan for days without, 0 for liquid, 1 for solid
prcp_type = np.zeros((len(df)))
df['prcp_type'] = pd.Series(prcp_type, index=df.index)
for i in range(len(df)):
    if df['solid'].iloc[i] > 0: # SOLID IS ONE
        df['prcp_type'].iloc[i] = 1
    elif df['liquid'].iloc[i] > 0: # LIQUID IS ZERO
        df['prcp_type'].iloc[i] = 0
    else: # ELSE, NAN
        df['prcp_type'].iloc[i] = np.nan

# Convert date to day of year        
df['date'] = pd.to_datetime(df['date']).apply(lambda x: x.strftime('%j')) # Change date column to datetime

# Save to CSV file
df.to_csv(YOUR_DIRECTORY + 'data.csv')
