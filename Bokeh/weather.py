from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

df=pandas.read_excel("verlegenhuken.xlsx")
x=df['Temperature']/10
y=df['Pressure']/10

plot_title="Temperature and Air Pressure"
x_axis_label="Temperature (˚C)"
y_axis_label="Pressure (hPa)"

f=figure(plot_width=500, plot_height=400)
f.title.text=plot_title
f.title.text_color = "Gray"
f.title.text_font_style="bold"
f.xaxis.axis_label = x_axis_label
f.yaxis.axis_label = y_axis_label

f.circle(x=x,y=y,size=1, line_color="#3288bd", fill_color="white")

output_file("Weather_plot.html")
show(f)

