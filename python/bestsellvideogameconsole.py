import pandas as pd
import pygal as pg
from pygal.style import Style
custom_style = Style(
background= '#f9f9fa',
colors= ('#d94e4c', '#e5884f', '#39929a', '#e27876', '#245d62', '#f0bb9b', '#c82d2a', '#234547'),
foreground= 'rgba(0, 0, 0, 0.9)',
foreground_strong= 'rgba(0, 0, 0, 0.9)',
foreground_subtle= 'rgba(0, 0, 0, 0.5)',
opacity= '.6',
opacity_hover= '.9',
plot_background= '#ffffff',)
data_10_seller = {}

### reference https://github.com/tanknk/PSIT-Project/blob/master/python/Top_20_ProPlayer_Prize_by_prize.py
data = pd.read_csv('https://github.com/Passakorn777/PSIT63/raw/main/data/CONSOLES.csv', encoding = "ISO-8859-1") # import file
data_top_prize = list(data['Sold (in Millon)'])
data_top_name = list(data['Name'])
for i in range(10):
    data_10_seller[data_top_name[i]] = data_top_prize[i]
data_10_seller = sorted(data_10_seller.items(), key=lambda x: x[1], reverse=True)

line_chart = pg.HorizontalBar(legend_at_bottom=True, legend_at_bottom_columns=5, fill=True, interpolate='cubic', style=custom_style)
line_chart.title = 'Top 10 Best-Selling Video Game Consoles (in Millions of Units sold)' # graph name
for i in data_10_seller:
    line_chart.add(i[0], i[1]) # create
line_chart.render_to_file('TopVideoGameConsolesSell.svg') # export file svg
