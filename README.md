# final-project-LB-SM-EM
final project Laura Bergedieck Shaun McMahon Enrique Mezo

# Languages we can use:
  jupyter, python, pandas, SQL,
  geopandas, django, matplotlib 

# Our data sources:
    1) LGAdisadvantageindex_2011: Economic disadvantage index of each area (via LGA = local government area i.e. neighborhood)
    2) Socialhousingtenencies_2016 (column R): Tenancies of social housing (characteristics):
    3) Socialhousingmaintenance_2016: Maintenance of social housing: amount of money spend per LGA
    4) Socialhousingvacancy_2016: Vacancy days for social housing: turnaround time for finding new residents
    5) QLD_LGA.shp: shapefile for LGAs in Queensland

# Our questions:
  We examine the situation of social housing in Queensland, Australia. We want to explore the following questions:

#  1) Compare the characteristics of different local government area (LGA):
  We merge three data sets for this using the LGA name in each data set: Socialhousingtenencies_2016 (column R), LGAdisadvantageindex_2011 (column A), Socialhousingmaintenance_2016 (column G)

  We want to create a dynamic table that allows a user to select a LGA and then displays the following information:
  a) population for that LGA
    -> match value from column B in LGAdisadvantageindex_2011
  b) economic disadvantage index (SEIFA) for that LGA
    -> match value from column I in LGAdisadvantageindex_2011
  c) number of housing units offered in that LGA
    -> count all the rows in data set Socialhousingtenencies_2016 for the selected LGA
  d) number of housing units with 1, 2 or 3+ bedrooms (count for each)
    -> in three different columns, count the number of housing units (rows) by bedroom type from column E (i.e. 1, 2 or 3+) in data set Socialhousingtenencies_2016 for the selected LGA
  e) average monthly rent
    -> in Socialhousingtenencies_2016, average over all units in column H for that LGA
  f) average monthly maintanance spendings
    -> in Socialhousingmaintenance_2016, sum up column C for that LGA
    -> and then devide by number of units for that LGA (as from part C, data set Socialhousingtenencies_2016)
  c) % overcrowded, % under-ocupied
    -> two different columns for % overcrowded and % under-ocupied housing units in that LGA (column I in data set Socialhousingtenancies_2016)

# 2) Create a map of Queensland showing the level of disadvantage by LGA and the total number of social housing units
  We join data sets Socialhousingtenencies_2016 file and LGAdisadvantageindex_2011 and shapefile called QLD_LGA.shp
  We create a Choropleth map showing:
  a) the disadvantage quintile per LGA as different colors
    -> from LGA disadvantage index_2011 column I
  b) show the number of social housing units per LGA (using dotdensity or some kind of call-out)

  -> Thought: it would be very cool, to click on the LGA and then be linked to the table in part 1) (not necessary though)

# 3) Vacancy of social housing unit by bedroom type
  We use data set Socialhousingvavancy_2016:  for this task
  We want to create a bar chart showing:
    y-axis: average number of vacant days
      -> average over column K per bedroom type in each LGA
    x-axis: per number of bedrooms in social housing unit
      -> from column B: 1, 2, 3, 4, 5, 6, 7
  Above the chart, display the following:
    max: LGA name with highest average number of vacant days
    min: LGA name with lowest average number of vacant days

# Website
We need to show our results in a website using Django


# Guidelines for this task:
  a) OPTIONAL: merge the data once and save it as CSV file (df.to_csv()).
      Alternatively, if it is feasible and fast, you can use only the existing sources (no cached data)
  b) Write at least one function that use the data to make plots or maps. Varying the inputs (for instance, the variable or the sample) should give me diverse outputs. In other words: there should be some sort of changeable parameters/selection/menu.
  c) Integrate that function into a lightweight web application, in Django. I should be able to navigate around and see a set of nice-looking plots through matplotlib or seaborn.
