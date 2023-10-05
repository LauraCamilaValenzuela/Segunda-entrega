import dash
import dash_bootstrap_components as dbc
from dash import html

#derecho = dbc.Container ([   
 #   html.H1('Datos del proyecto'),
   # html.Hr(),
    #html.H2('Ensayos de pentracion'),
    #dbc.Row([ 
     #   dbc.Col ('visualizacion',md=3 , style={'background-color':'black'}),
      #  dbc.Col ('texto',md=6 , style={'background-color':'gray'}),
       # dbc.Col ('Usuario',md=3 , style={'background-color':'blue'})
    
   # ])
 # ])

derecho = dbc.Container(
    [
        html.Hr(),
        html.H2('Datos del proyecto', style={'color':'White'}),
        html.Hr(style={'color':'White'}),
        html.Label('Nombre:', style={'color':'White'}),
        dbc.Input(value="Nombre"),
        html.Label('Localización:', style={'color':'White'}),
        dbc.Input(value="Localización"),
        html.Label('Fecha Inicio:', style={'color':'White'}),
        dbc.Input(value="Fecha", type="date"),
        html.Label('Fecha Fin:', style={'color':'White'}),
        dbc.Input(value="Fecha", type="date"),
        html.Hr(),
    ])