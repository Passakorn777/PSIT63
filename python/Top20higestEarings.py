import pandas as pd
import pygal as pg
from pygal.style import Style
custom_style = Style(
  background='#fdf6e3',
  plot_background='#eee8d5',
  foreground='#657b83',
  foreground_strong='#073642',
  foreground_subtle='#073642',)
data_20_prize = {}

#ref code from https://github.com/tanknk/PSIT-Project/blob/master/python/Top_20_ProPlayer_Prize_by_prize.py
data = pd.read_csv('https://github.com/Passakorn777/PSIT63/raw/main/data/Top100HighestOverallEarnings.csv', encoding = "ISO-8859-1") # import file
data_top_prize = list(data['Total (Overall)'])
data_top_name = list(data['Player ID'])
for i in range(20):
    data_20_prize[data_top_name[i]] = data_top_prize[i]
data_20_prize = sorted(data_20_prize.items(), key=lambda x: x[1], reverse=True)

line_chart = pg.HorizontalBar(fill=True, interpolate='cubic', style=custom_style)
line_chart.title = 'Top 20 Pro Player with the highest reward prize (in Dollars)' # graph name
for i in data_20_prize:
    line_chart.add(i[0], i[1]) # create
line_chart.render_to_file('Top20HighestEarnings.svg') # export file svg