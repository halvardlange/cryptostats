#!/usr/local/bin/python
import plotly.offline as py
import plotly.graph_objs as go
import json
import math
import pandas as pd
import os

try:
    os.chdir('/Users/halvard/Documents/GeekToolScripts')
except Exception as e:
    print e

data_raw = pd.read_json("https://api.coinmarketcap.com/v1/ticker/?limit=20")
data = data_raw.sort_values('percent_change_24h',ascending = False)
data['colors']=-data['percent_change_24h']

#print data[['name','price_usd','percent_change_24h']]

y_text = []
for index, row in data.iterrows():    
    y_text.append(('{percent_change_24h:.2f} %').format(percent_change_24h=row['percent_change_24h']))

trace1 = go.Bar(
    x=data['symbol'],
    y=data['percent_change_24h'],
    #text = y_text,
    #textposition = 'auto',
    #textfont=dict(family='Arial', size=14, color='rgba(245, 246, 249, .70)'),
    opacity = 1.0,
    marker=dict(
        color = data['colors'],
        colorscale = 'Jet',
    )
)

data = [trace1]
layout = go.Layout(
    title = '% Change Last 24 Hours',
    titlefont=dict(
        color='rgb(255, 255, 255)'),
    xaxis=dict(
        #title='Coin',
        gridcolor='transparent',
        #range=[-2, 6],
        #type='log',
        tickcolor = 'rgb(255, 255, 255)',
        color = 'rgb(255, 255, 255)',
        tickwidth = 1.45,
        zerolinewidth=0,
        ticklen=5,
        gridwidth=0,
    ),
    yaxis=dict(
        title='Percent Change (24h)',
        gridcolor='transparent',
        tickcolor = 'rgb(255, 255, 255)',
        #type = 'log',
        color = 'rgb(255, 255, 255)',
        tickwidth = 1.45,
        showbackground = False,
        #range=[2,12],
        zerolinewidth=0,
        ticklen=5,
        gridwidth=0,
    ),
    paper_bgcolor='rgb(243, 243, 243,0.1)',
    plot_bgcolor = 'transparent',
)

fig = go.Figure(data=data, layout=layout)

try:
    py.plot(fig, filename='percent_change_bar_graph.html', auto_open = False, show_link=False)
except Exception as e:
    print e
