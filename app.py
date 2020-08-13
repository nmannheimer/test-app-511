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

fig = px.histogram(cars, x='Origin', y='MPG',
                   color='Origin',
                   histfunc='avg',
                   range_y=[0,60],
                   animation_frame='Model')

fig2 = px.scatter(cars, x="MPG", y="Weight", color="Origin", size='Horsepower')

fig3 = px.parallel_coordinates(cars,
                              color='MPG',
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=25)
fig4 = px.box(cars, x='Model', y='MPG', color='Origin')

app.layout = html.Div(children=[
    html.H1(children='Automobile Exploration'),

    html.Div(children='''
        Understand Key Performance Trends in the Cars Dataset
    '''),
    html.Div([
        dcc.Graph(
            id='bar-chart',
            figure=fig
        ),
        dcc.Graph(
            id='scatter-plot',
            figure=fig2
        ),
    ], style={'display': 'inline-block', 'width': '49%'}),
    html.Div([
        dcc.Graph(
            id='box',
            figure=fig4
        ),
        dcc.Graph(
            id='parallel-coordinates',
            figure=fig3
        ),

    ], style={'width': '49%', 'display': 'inline-block'})
])

if __name__ == '__main__':
    app.run_server(debug=True)






















