from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x=[0,2,3,4,5,6,8]
y=[0,9,9,8,10,11,12]


output_file("Line.html")

#create a figute object
f=figure()
u=figure()
v=figure()

#create a line plot
f.line(x,y)
u.triangle(x,y,10)
v.circle(x,y)

#wright the plot to the figure object
show(f)
show(u)
show(v)





