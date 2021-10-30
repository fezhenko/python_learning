from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

df = pandas.read_csv("adbe.csv",parse_dates=['Date'])
f=figure(width=500,height=500, x_axis_type='datetime')
f.line(df['Date'], df['Close'], color="Orange", alpha=0.5)
output_file("ogo.html")
show(f)