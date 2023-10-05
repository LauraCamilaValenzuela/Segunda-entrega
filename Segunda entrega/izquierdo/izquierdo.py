import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

izquierdo = dbc.Container ([
    html.Hr(),   
    html.H1('DATOS DE LA ESTRUCTURA'),
    html.Hr(),
    html.Div([
        html.Label('Número de plantas de la estrutura', style={'fontSize': '30px'}),
        html.Hr(style={'color':'lightgray'}),
        dcc.Input(id='entradaPisos', value = 5, type = 'number'),
        html.Hr(style={'color':'lightgray'}),
        html.Label(id='salidaPisos')

    ])
  ])