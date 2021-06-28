#Below we import a csv file as data input instead of using lists
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

#we now have to use pandas to open up the file create a dataframe from the csv output_file
df1=pd.read_csv('sample.csv')

#after the dataframe is create we map variables to the x and y columns:
x=df1['x']
y=df1['y']

output_file('csv_line_test.html')

f=figure()

f.line(x,y)

show(f)
