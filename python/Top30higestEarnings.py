import pandas as pd
import pygal as pg
data_30_prize = {}

data = pd.read_csv('https://github.com/Passakorn777/PSIT63/raw/main/data/Top100HighestOverallEarnings.csv', encoding = "ISO-8859-1") # import file
data_top_prize = list(data['Total (Overall)'])
data_top_name = list(data['Player ID'])
for i in range(30):
    data_30_prize[data_top_name[i]] = data_top_prize[i]
data_30_prize = sorted(data_30_prize.items(), key=lambda x: x[1], reverse=True)

line_chart = pg.HorizontalBar()
line_chart.title = 'Top 30 Pro Player with the highest reward prize (in Dollars)' # graph name
for i in data_30_prize:
    line_chart.add(i[0], i[1]) # create
line_chart.render_to_file('Top100HighestOverallEarnings.svg') # export file svg