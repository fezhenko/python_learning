from bokeh.plotting import output_file, show, figure
from bokeh.models import HoverTool, ColumnDataSource
import pandas

# x = [1, 2, 3, 4, 5]
# y1 = [6, 7, 2, 4, 5]
# y2 = [2, 3, 4, 5, 6]
# y3 = [4, 5, 5, 7, 2]
#
# p=figure(title="Multiple glyphs example", x_axis_label="x", y_axis_label="y")
# p.vbar(x=x, top=y2, legend_label="Rate", width=0.5, bottom=0, color="red")
#
# output_file('plotting_by_csv.html')
# show(p)

# file = pandas.read_csv("Sample_of_the_produced_time_values.csv", parse_dates=['Start', 'End'])
file = pandas.read_csv("Sample_of_the_produced_time_values.csv", parse_dates=['Start', 'End'])
file['Start2'] = file['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
file['End2'] = file['End'].dt.strftime("%Y-%m-%d %H:%M:%S")

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_width", title="My Plot")
p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start2"), ("End", "@End2")])
p.add_tools(hover)

q = p.quad(left=file['Start'], right=file['End'], bottom=0, top=1, color='green')

output_file("plotting_time_intervals_from_csv.html")
show(p)
