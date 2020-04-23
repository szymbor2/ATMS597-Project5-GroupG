## ATMS Project 5 (Group G)

This document details the procedure followed to create the Regression-based Classification model to predict the precipitation type for St.Cloud, Minnesota. Here are the main steps:

## 1) DATA CLEANUP

The input data consists of monthly metar files at 5-minute resolution downloaded from the following NOAA-NCDC ftp server:
ftp://ftp.ncdc.noaa.gov/pub/data/asos-fivemin/

The data was downloaded by wget using recursive loops over each successive month and each succesive year, for the given station (KSTC):

wget ftp://ftp.ncdc.noaa.gov/pub/data/asos-fivemin/6401-{2000..2019}/64010KSTC{2000..2019}{01..12}.dat

Once downloaded, the data was read by a simple python code that parsed through the complicated text formatting to filter out the information neede for our analysis.This included:
1) Wind data (Speed, Direction, Gusts, Variability in direction)
2) Temperature, Dewpoint and Relative Humidity
3) Precipitation Amounts
4) Precipitation types (Frozen and Liquid Categories)

Missing data and Unicode Errors while reading meant a few data had to be thrown away. The usable data were stored in csv files for each of the months as in the original data.




