#import the needed libraries
import numpy as np
import plotly.graph_objects as go

#set seed for random number generation
np.random.seed(1234)

#Generate random numbers
random_x=np.linspace(0, 100, 100)
random_y0=np.random.randn(100) +5
random_y1=np.random.randn(100)
random_y2=np.random.randn(100) -5

fig = go.Figure()

fig.add_trace(go.Scatter(x=random_x,y=random_y0,mode='markers',name='markers'))
fig.add_trace(go.Scatter(x=random_x,y=random_y1,mode='lines',name='lines'))
fig.add_trace(go.Scatter(x=random_x,y=random_y2,mode='lines+markers',name='lines+markers'))
#To just show without saving the file
#fig.show()

#To save the file
fig.write_html('scatter_figure1.html', auto_open=True)
