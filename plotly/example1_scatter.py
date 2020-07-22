import plotly
print('Hello World')
print("Print print print")
print(plotly.__version__)

import plotly.graph_objects as go
fig = go.Figure(data=go.Scatter(x=[1,2,3],y=[20, 30, 11],mode='markers'))
#fig = go.Figure(data=go.Histogram(x=[1,2,3],y=[2, 3, 1]))

#To just show without saving the file
#fig.show()

#To save the file
fig.write_html('scatter_figure.html', auto_open=True)
