import dash
import dash_bootstrap_components as dbc
from dash import html

navegador = dbc.Container ([   
    html.Hr(),
    html.H2('NÚMERO DE EXPLORACIONES GEOTECNICAS'),
    html.Hr(),
    html.H2('NSR 10'),
    html.Hr(),
    html.H4('''Este aplicativo te permite calcular el numero de sondeos y su profundidad,'''),
    html.H4('''con base en el área del proyecto, la cantidad de niveles y su carga.'''),
    html.Hr(),
   # dbc.Row([ 
    #    dbc.Col ('visualizacion',md=3 , style={'background-color':'white'}),
     #   dbc.Col ('texto',md=6 , style={'background-color':'white'}),
      #  dbc.Col ('Usuario',md=3 , style={'background-color':'white'})
    
    #])
  ])