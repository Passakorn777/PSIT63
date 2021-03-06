import pandas as pd
import pygal as pg
from pygal.style import Style
custom_style = Style(
  background='#fdf6e3',
  plot_background='#eee8d5',
  foreground='#657b83',
  foreground_strong='#073642',
  foreground_subtle='#073642',)
data_20_topteam_earnings = {}

#soure code from https://github.com/tanknk/PSIT-Project/blob/master/python/Top_20_ProPlayer_Prize_by_prize.py
data = pd.read_csv('https://github.com/Passakorn777/PSIT63/raw/main/data/Top100highestteamesportearning.csv', encoding = "ISO-8859-1") # import file
data_top_prize = list(data['TotalUSDPrize'])
data_top_name = list(data['Name'])
for i in range(20):
    data_20_topteam_earnings[data_top_name[i]] = data_top_prize[i]
data_20_topteam_earnings = sorted(data_20_topteam_earnings.items(), key=lambda x: x[1], reverse=True)

line_chart = pg.HorizontalBar(fill=True, interpolate='cubic', style=custom_style)
line_chart.title = 'Top 20 Team esport earnings the highest reward prize (in Dollars)' # graph name
for i in data_20_topteam_earnings:
    line_chart.add(i[0], i[1]) # create
line_chart.render_to_file('Top20teamesportearnings.svg') # export file svg