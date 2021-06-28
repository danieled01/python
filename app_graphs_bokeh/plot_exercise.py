from bokeh.plotting import figure, output_file, show
import pandas as pd

# output to static HTML file
output_file("plot_exercise.html")
df1=pd.read_excel('verlegenhuken.xlsx', sheet_name='Ark1')
x=df1['Temperature']
y=df1['Pressure']/10
p = figure(plot_width=500, plot_height=500)

# add a circle renderer with a size, color, and alpha
p.circle(x,y, size=1, color="navy", alpha=0.5)

# show the results
show(p)
