# Plot-data-from-Mysql Tables and excel

#Given a excel sheet, Create MySql Database and Plot Data.

Find cumulative distribution function (CDF) of company data and Plot it for each Company.

Task 0:
Populate Company-Parameter data for all months in mysql tables

Task 1.
Company Rating =
[a1*param1+a2*param2+a3*param3+a4*param4+a5*param5+a6*param6+a
7*param7+a8*param8+a9*param9+a10*param10]/[a1+a2+a3+a4+a5+a6+a7
+a8+a9+a10]
Where:
a1=7.1
a2=1.2
a3=3.1
a4=0.9
a5=4.5
a6=0.28
a7=0.56
a8=0.81
a9=1.6
a10=2
Calculate Company Rating for all companies each month

Task 2:
Company relative score
Now we will arrange these company ratings in a normal distribution, so that they are placed
relative to each other and we may know how our scores are distributed. For that we
calculate: Company relative score
= score of a company in relation to all companies that month in a normal distribution
(Cumulative distribution function in python)
Cumulative distribution of a number for an array is defined as: y=cdf
X= company rating for company number i
Mu= mean of company rating of all the companies that month
Sigma = standard deviation of company rating of all the companies that month
Company relative score = 100*y

Task 3:
1. Calculate company relative score(CRS) for each company in each of the months
2. Graphical representation:
We have to Plot CRS for each company month on month
That is: For each company draw a graph with months1 to month12 on x axis and
respective CRS for that month on y axis

