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
dic = {}
#source code form https://github.com/tanknk/PSIT-Project/blob/master/python/Top_Team.py
data = pd.read_csv("https://github.com/Passakorn777/PSIT63/raw/main/data/COMPANIES.csv", encoding = "ISO-8859-1") # import file
data_top = data[:10] # filter
data_top_name = data_top['Name'] # Name companies
data_top = data_top['Revenue (in Billon)'] # Total Revenue

for i in range(10):
    dic[data_top_name[i]] = data_top[i] # create dict
line_chart = pg.HorizontalBar(fill=True, interpolate='cubic', style=custom_style) 
line_chart.title = 'The 10 Biggest Video Games Companies Revenue in the World(in Billon)' # graph name

for i in data_top_name:
    line_chart.add(i, dic[i]) # create
line_chart.render_to_file('topcompanies.svg') # export file svg
