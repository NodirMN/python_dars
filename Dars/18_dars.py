# 18 dars. Statistica
import pygal 

line_chart = pygal.Line()
line_chart.title = 'Statistica'
line_chart.x_labels =['Fevral', 'Mart', 'Aprel', 'May']
line_chart.add('Fackebook', [9.24, 13.7, 16.24, 18.07])
line_chart.add('Instagram',  [24.03, 21.3, 22.4, 15.13])
line_chart.add('YouTube', [33.8, 27.1, 12.8, 8.13])
line_chart.render_in_browser()
