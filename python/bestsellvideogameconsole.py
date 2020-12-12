import pandas as pd
import pygal as pg
from pygal.style import Style
custom_style = Style(
background= '#0e4448',
colors= ('#93d2d9', '#ef940f', '#8C6243', '#fff', '#48b3be', '#f4b456', '#b68866', '#1b8088'),
foreground= 'rgba(255, 255, 255, 0.9)',
foreground_strong= 'rgba(255, 255, 255, 0.9)',
foreground_subtle= 'rgba(255, 255 , 255, 0.5)',
opacity= '.5',
opacity_hover= '.9',
plot_background= '#0d3c40',
transition= '250ms ease-in',)
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
