## ATMS Project 5 (Group G)
### Arka Mitra, Sarah Szymborski, and Jeff Thayer

This document details the procedure for using supervised classification techniques from the sklearn Python package to predict liquid and frozen precipitation types for St. Cloud, Minnesota (KSTC) over the period 2000 through 2019. The observational dataset from KSTC was separated into training and testing periods using a 70-30 split. Logistic Regression and Ensemble Random Forest were the models of choice, with the predictive ability of each model determined through Brier Skill Scores. Here are the main steps:

## 1) DATA CLEANUP

The input data consists of monthly metar files at 5-minute resolution downloaded from the following NOAA-NCDC ftp server:
ftp://ftp.ncdc.noaa.gov/pub/data/asos-fivemin/

The data was downloaded by wget using recursive loops over each successive month and each succesive year, for the given station (KSTC):

  wget ftp://ftp.ncdc.noaa.gov/pub/data/asos-fivemin/6401-{2000..2019}/64010KSTC{2000..2019}{01..12}.dat

Once downloaded, the data was read by a simple python code that parsed the complicated text formatting to filter out the information needed for our analysis. This included:

  1) Wind data (Speed, Direction, Gusts, Variability in direction)
  2) Temperature, Dewpoint and Relative Humidity
  3) Precipitation Amounts
  4) Precipitation types (Frozen and Liquid Categories)

Additional variables used for prediction were day of the year and time of day. The existence of missing data and unicode errors in the observations meant some data had to be thrown out. The usable data were stored in csv files for each of the months as in the original data. When combining all csv files into a comprehensive one, frozen precipitation was set to 0, liquid to 1, and non-precipitating days were removed.

## 2) READING AND ADJUSTING INPUT DATA

The comprehensive csv file was read using pandas. The date column was converted to datetime in terms of day of the year, and then various columns were dropped when checking the ability of each model. The remaining data was filtered for NaN values, resulting in the final subset used for predicting precipitation type. 

## 3) IMPLEMENTING CLASSIFICATION TECHNIQUES

With the final subset of the observational data determined, the testing and training periods were separated using a 70-30 split. Logistic Regression and Ensemble Random Forest models were then implemented via the sklearn package. The predictive skill of each model was ascertained using calculated Brier Skill Scores between each model and climatology (i.e. reference forecast), with values closer to 1 indicating greater relative skill at predicting frozen or liquid precipitation compared with the skill when using climatology.
