import pandas as pd
import pygal as pg
data_100_prize = {}

data = pd.read_csv("Top-100-Highest-Overall-Earnings.csv") # import file
data_top_prize = list(data['Total (Overall)'])
data_top_name = list(data['Player Name'])
for i in range(100):
    data_100_prize[data_top_name[i]] = data_top_prize[i]
data_100_prize = sorted(data_100_prize.items(), key=lambda x: x[1], reverse=True)

line_chart = pg.HorizontalBar()
line_chart.title = 'Top 20 Pro Player with the highest reward prize (in Dollars)' # graph name
for i in data_100_prize:
    line_chart.add(i[0], i[1]) # create
line_chart.render_to_file('Top-100-Highest-Overall-Earnings.csv') # export file svg