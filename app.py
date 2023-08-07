import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import joblib
from google.cloud import bigquery
import db_dtypes
import time

# import dash & bootstrap libraries

import dash
from dash import Dash, dcc, html, Output, Input, State, callback
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from plotly.subplots import make_subplots

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

risk_options = [
    {'label': 'Low', 'value': 'Low'},
    {'label': 'Medium', 'value': 'Medium'},
    {'label': 'High', 'value': 'High'}
]

# App Layout

app.layout = html.Div(children=[
    html.Div(
        style={
            'padding-top': 20,
            'padding-bottom': 40,
            'text-align': 'center',
            'backgroundColor': "white",
        },
        children=[
            html.Img(src="assets/JFF.jpg", height="60px"),
            html.Header(id='name-output',
                style={
                    'color': 'black',
                    'font-weight': "bold",
                    'fontSize': 36,
                    'margin-top': 12
                }
            ),
#            dbc.RadioItems(
#                id="radios",
#                className="btn-group",
#                inputClassName="btn-check",
#                labelClassName="btn btn-outline-dark",
#                labelCheckedClassName="active",
#                style={'marginTop': 14},
#                options=[
#                    {"label": "Client Information", "value": 1},
#                    {"label": "Market Information", "value": 2},
#                    {"label": "Advisor Information", "value": 3},
#                ],
#                value=1,
#            ), 
        ]
    ), 
    dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    width=2,
                    children=[
                        html.Div(
                            style={
                                'padding-top': 20,
                                'padding-bottom': 25,
                                'padding-left': 10
                            },
                            children=[
                                dbc.Input(id='name-input', placeholder='Client Name', type='text', style={'marginTop':14}),
                                #html.Br(),
                                #html.P(id='name-output'),
                                dbc.Input(id='portfolio-input', placeholder='# of Accounts', type='number', step='1', min='0',  style={'marginTop':14}),
                                #html.Br(),
                                #html.P(id='portfolio-output'),
                                #dcc.Dropdown(
                                #    id='risk-dropdown',
                                #    style={'marginTop': 14, 'color': 'black'},
                                #    options=risk_options,
                                #    optionHeight=55,
                                #    placeholder='Risk Type'
                                #),
                                #html.Br(),
                                #html.P(id='risk-dropdown-output')
                            ]
                        ),
                    ],
                    style={'backgroundColor': 'black', 'color': 'white'},
                ),
                dbc.Col(
                    width=2,
                    style={'backgroundColor': 'darkblue', 'color': 'white'},
                    children=[
                        html.P('For account information')
                    ]
                ),
                dbc.Col(
                    children=[
                        html.H4(children='', id='chart-description',
                        style= {'text-align':'left', 'padding-top':25, 'padding-left':15}),
                        #dcc.Graph(id='fig1'),
                        html.P(children='', id="analysis"),
                    ],
                    width={"size":8},
                    style={'backgroundColor': 'darkslateblue'}
                )
            ]
        )
    ]
    )
])

# input callbacks

@app.callback(Output("name-output", "children"), [Input("name-input", "value")])
def output_text(value):
    if value is not None:
        return str(value)
    else:
        return ''

@app.callback(Output("portfolio-output", "children"), [Input("portfolio-input", "value")])
def output_text(value):
    if value is not None:
        return "Portfolio Value: $" + str(value)
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)