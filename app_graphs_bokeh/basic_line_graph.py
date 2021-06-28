#we create a new line graph using bokeh - this really basic but its a good representation of the backbone.
from bokeh.plotting import figure
from bokeh.io import output_file, show

#create some data to represent in a graph
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#prepare the output_file
output_file('line_test.html')

#create figure object
f=figure()

#create a line plot
f.line(x,y)

#show the graph
show(f)
