# Convert reviewed files into a big CSV file
# Make sure to set working directory

import pandas as pd
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
prcp_type = np.empty((0))
for i in range(len(df)):
    print(df.iloc[i])
    if df['solid'].iloc[i] > 0: # SOLID IS ONE
        prcp_type = np.append(prcp_type, 1)
    elif data['liquid'].iloc[i] > 0: # LIQUID IS ZERO
        prcp_type = np.append(prcp_type, 0)
    else:
        prcp_type = np.append(prcp_type, np.nan) # ELSE, NAN
    break
df['prcp_type'] = pd.Series(prcp_type, index=df.index)

# Save to CSV file
df.to_csv(YOUR_DIRECTORY + 'data.csv')
