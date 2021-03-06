# -*- coding: utf-8 -*-
"""Python-Dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Cbi5tn5aIsUU9a-Hk4IMMYdJgc4FRfx
"""

pip install dash

import dash
import plotly.express as px
import pandas as pd

## Data Exploration with Pandas

df = pd.read_csv("/content/vgsales.csv")

df.head()

df.iloc[:5,[2,3,5,10]]

df.Genre.nunique()

df.Genre.unique()

sorted(df.Year.unique())

## Data Visualization with Plotly

fig_pie = px.pie(data_frame=df, names='Genre', values='Japan Sales')
fig_pie.show()

fig_pie = px.pie(data_frame=df, names='Genre', values='North American Sales')
fig_pie.show()

fig_bar = px.bar(data_frame=df, x='Genre', y='World Sales')
fig_bar.show()

fig_hist = px.histogram(data_frame=df, x='Year', y='World Sales')
fig_hist.show()

## Interactive Graphing with Dash

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input

app = dash.Dash(__name__)

app.layout = html.Div([
                       html.H1("Graph Analysis with Charming Data"),
                       dcc.Dropdown(id='genre-choice', options=[{'label':x, 'value':x}
                                                                for x in sorted(df.Genre.unique())],
                                    value='Sports'),
                       dcc.Graph(id='my-graph',figure={})
                       
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='genre-choice', component_property='value')
)
def interactive_graphing(value_genre):
  print(value_genre)
  dff = df[df.genre==value_genre]
  fig = px.bar(data_frame=dff,x='Year',y='World Sales')
  return figure

if __name__=='__main__':
  app.run_server()