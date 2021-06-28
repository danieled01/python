from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

df1=pd.read_csv('bachelors.csv')

x=df1['Year']
y=df1['Engineering']

output_file('degrees.html')

f=figure()

f.line(x,y)

show(f)
