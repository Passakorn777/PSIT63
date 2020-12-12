import pandas, numpy, pygal
from pygal.style import Style
custom_style = Style(
  background='#fdf6e3',
  plot_background='#eee8d5',
  foreground='#657b83',
  foreground_strong='#073642',
  foreground_subtle='#073642',)
# ref code from https://github.com/tanknk/PSIT-Project/blob/master/python/overallprizemoneybygames.py
def main():
    """ arrange data """
    dataFrame = pandas.read_csv('https://github.com/Passakorn777/PSIT63/raw/main/data/PRIZE.csv', encoding = "ISO-8859-1")
    data = numpy.array(dataFrame[['Name','Prize']]).tolist()
    graph(data)
def graph(data):
    """ plot graph """
    line_chart = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=5,fill=True, interpolate='cubic', style=custom_style)
    line_chart.title = 'Top 20 Games Awarding Prize Money (in Dollars)'
    for i in range(20):
        line_chart.add(str(data[i][0]), [{'value': int(data[i][1]), 'label': '{:.2f}%'.format(100*int(data[i][1])/sum([j[1] for j in data]))}])
    line_chart.render_to_file('TopGameAwardPrize.svg')  

main()