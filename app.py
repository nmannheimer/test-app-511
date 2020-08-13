import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

cars = pd.read_csv("original cars.csv", sep=";")

colors = {'US':1, 'Europe':2, 'Japan':3}
cars['Origin_col'] = [colors[i] for i in cars['Origin']]

fig = px.bar(cars, x='Origin', y='MPG', color='Origin')

fig2 = px.scatter(cars, x="MPG", y="Weight", color="Origin")

fig3 = px.parallel_coordinates(cars,
                              color='Origin_col',
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2)

app.layout = html.Div(children=[
    html.H1(children='Automobile Exploration'),

    html.Div(children='''
        Understand Key Performance Trends in the Cars Dataset
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),
    dcc.Graph(
        id='example-graph3',
        figure=fig3
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)








