Legal Innovators, LLC.
University of Connecticut Werth Institute

-----------------------------------------
Version: 1.00.00
Last Updated: May 20, 2020
-----------------------------------------

-----------------------------------------
Directories:
## Archive - Old scripts used in early
## prototyping and development. Not to
## be used for full implementation.
##
## Create_Data - Containts the file
## create_data_v2.py which can be used
## to rapidly generate mock data with 
## downstream scoring correlations. This
## data is then saved to a csv in the 
## same directory.
##
## Out - Directory that stores outputs of
## machine learning tests.
##
## Out_Archive - Optional directory that 
## can be utilized for storing past 
## tests. A sample directory containing a
## test using 10,000 samples is kept 
## there.
##
## Scripts - Directory for performing 
## machine learning tests. This can be 
## done directly using main.py or 
## manually using individual scripts, as
## stated below.
-----------------------------------------

-----------------------------------------
Testing using main.py
## Selecting Models
## To select the models being run in the 
## test, rapid addition is possible 
## through the use of learn objects. 
## These objects take a name as a string
## and a lambda_code variable that 
## accepts a sklearn machine learning
## method. Three models are pre-loaded 
## into the main function.
##
## Importing Data and Setting Parameters
## The data can be quickly loaded through
## including the file in the same 
## directory and specifying its name, or
## setting its full path into the file
## variable. Several parameters have to 
## be clarified to the program so that 
## it appropriately handles the data in 
## preprocessing.
## 
## identifier_1 and identifier_2 
## Two categorical columns from the
## csv that are used in the unbiasing/
## normalization process. These
## categories split the data into the 
## number of groups created; therefore,
## these should be low-count categories. 
## The preset values are gender (2) and
## ethnicity (4), creating 8 (2*4) 
## normalization groups. 
##
## categorical
## All the columns from the csv that 
## contain non-floats and non-integers.
## 
## success
## The column used by the learning 
## algorithms for determining outputs
##
## correlating
## The column users believe best 
## correlates with the success variable.
## This is used for normalization 
## purposes.
##
## restriction
## Columns users want to run tests on 
## using limited data. These columns are
## then the only ones used as traits in
## the learning algorithms.
##
## Tests are then performed and output 
## into the Out directory. Make sure to
## remove previous test data from the Out
## directory before performing another 
## test.
-----------------------------------------

-----------------------------------------
Reports
## Reports can be customized by adjusting
## Generate_Report.py. At the moment, 
## reports create a directory containing 
## a file with metrics and the data used
## to perform those metrics to increase
## reproducability. Additionally heatmaps
## for the specified confusion matrix are
## included in the directory as well.
-----------------------------------------

-----------------------------------------
Contributors:
Patrick Hocking 
(patrick.hocking@uconn.edu)
Rojaun Samuda
(rojaun.samuda@uconn.edu)
William Boafo
(william.boafo@uconn.edu)
Shihab Khalifa
(shihab.khalifa@uconn.edu)
-----------------------------------------