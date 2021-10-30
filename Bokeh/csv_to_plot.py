import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show


#crear dataframe object and create 2 objects for each column
df=pandas.read_csv("bachelors.csv")
x=df['Year']
y=df['Engineering']

#Name our output html
output_file("csv_to_plot.html")

#create a figute object
f=figure()

#create a line plot
f.line(x,y)

#wright the plot to the figure object
show(f)






