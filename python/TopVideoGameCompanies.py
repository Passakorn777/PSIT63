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
