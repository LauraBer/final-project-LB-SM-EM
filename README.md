# final-project-LB-SM-EM
final project Laura Bergedieck Shaun McMahon Enrique Mezo

# Languages we used:
  jupyter, python, pandas,
  geopandas, django, matplotlib

# Our data sources:
We used five different data sources, listed below. The sources are linked in our website, in the "Background" section.
  1) csv.file: Tenancies of social housing and their characteristics per LGA (neighborhood)
  2) csv.file: Amount of money spend on maintenance per LGA
  3) csv.file: Vacancy days for social housing measured in turnaround time for finding new residents
  4) csv.file: Economic disadvantage index of each area (via LGA = local government area i.e. neighborhood) measured in quintiles across all LGAs in Queensland
  5) Shapefile: Shapefile for LGAs in Queensland

# Our questions & corresponding analysis:

We examine the situation of social housing in Queensland, Australia. We explore the following three questions:
#  1) Compare the characteristics of different local government area (LGA): see file Question1.ipynb for code
  We want to create a dynamic table that allows a user to select a LGA and then displays the information listed below.
  For the data cleaning process, we we merge three data sets (Tenencies, SEIFA disadvantage index, Maintenance). We used the LGA name in each data set as our index to create a clean csv.file called housing.csv.
  For the data cleaning, we worked with jupyter notebook and pandas; the code can be found in the file Question1.ipynb.
  The table should display:
  a) population for that LGA
    -> from SEIFA disadvantage index
  b) economic disadvantage index (SEIFA) for that LGA
    -> from SEIFA disadvantage index
  c) number of housing units offered in that LGA
    -> from Tenenancies, count all the rows (social housing units) in data set for the selected LGA
  d) number of housing units with 1, 2 or 3+ bedrooms (count for each)
    -> from Tenenancies, count the number of housing units (rows) by bedroom type in data set Socialhousingtenencies_2016 for the selected LGA (display in three different columns)
  e) average monthly rent
    -> from Tenenancies, average the rent over all units per LGA
  f) average monthly maintanance spending
    -> from Maintenance, sum up all spending per LGA
    -> and then devide by number of units for that LGA
  g) % overcrowded, % under-ocupied
    -> from Tenancies, create the % values for overcrowded and under-ocupied housing units per LGA

# 2) Create a map of Queensland showing the level of disadvantage by LGA: see file Question2.ipynb for code
We use the SEIFA disadvantage index data set and the shapefile for LGAs in Queensland to create a map showing:
  a) the disadvantage quintile per LGA as different colors for each quintile
Limitations/ Thoughts for further work:
  b) We would have liked to display the names of LGAs on the map (e.g. when hovering over it). This exercise was out of our capacities and time limits of this project.
  c) We would have liked to display the total number of social housing units per LGA on the same map, to somehow compare supply of social housing with economic disadvantage of that neighborhood (using dotdensity or some kind of call-out when hovering over the LGA). This was out of the scope of this project as well.

# 3) Vacancy of social housing unit by bedroom type: see file Question3.ipynb for code
  We use the Vacancy data set for this task.
  We want to create a bar chart showing the average number of days that different size properties are vacant for selected LGAs (ideally dynamic with dropdown selection). We have included the four most populated LGAs in our graph to compare them against the overall mean. Against the wide spread opinion that there is too much supply of multiple-bedroom properties and they are not fully used, we found that these properties have fewer vacancy days than properties with less bedrooms. 
    y-axis: average number of vacant days
    x-axis: bedroom type (all bedroom types, 1, 2, 3, 4+ bedrooms)
It would have been nice to include a dynamic feature to change this chart for different LGAs, but we did not get there yet.

# Website
We worked based on the Django-ex folder used for homework 6 and created our own Django-final folder. 
Inside this, we created a view called projectview.py.
We created two templates: website.html and headers.html. Also, we saved the created files from Q1, Q2, and Q3 in the static folder.
We amended the files models.py and forms.py, to be able to create the dropdown menu for question 1.
We did not clean up the entire folder, as while trying to do so we broke the code somewhere, and therefore rather left all the examples in order to not delete a file that is needed for the website to run.
