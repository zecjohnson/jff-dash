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
server = app.server

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
                                dbc.Input(id='accountno-input', placeholder='# of Accounts', type='number', step='1', min='0',  style={'marginTop':14}),
                            ]
                        ),
                    ],
                    style={'backgroundColor': 'black', 'color': 'white'},
                ),
                dbc.Col(
                    width=2,
                    style={'backgroundColor': 'darkblue', 'color': 'white'},
                    children=[
                        html.Div(
                            id='account-sections',
                            style={
                                'padding-top': 20,
                                'padding-bottom': 25,
                                'padding-left': 10
                            },
                        )
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

@app.callback(
Output('account-sections', 'children'),
[Input('accountno-input', 'value')]
)
def generate_account_sections(num_accounts):
    sections = []
    if num_accounts:
        for i in range(num_accounts):
            section = html.Div(
                style={'margin-top': 20},
                children=[
                    dbc.Input(id=f'name-input-{i}', placeholder='Client Name', type='text', style={'marginTop': 14}),
                    dbc.Input(id=f'portfolio-input-{i}', placeholder='# of Accounts', type='number', step='1', min='0',
                              style={'marginTop': 14}),
                    dbc.Input(id=f'risk-dropdown-{i}', placeholder='Risk Type', type='text', style={'marginTop': 14}),
                ]
            )
            sections.append(section)
    return sections

if __name__ == '__main__':
    app.run_server(debug=True)
