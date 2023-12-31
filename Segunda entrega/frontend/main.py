import dash
import dash_bootstrap_components as dbc

from navegador.navegador import navegador
from derecho.derecho import derecho
from izquierdo.izquierdo import izquierdo

layout = dbc.Container ([
    dbc.Row([ 
        dbc.Col (navegador,md=12 , style={'background-color':'White'}),
        dbc.Col (izquierdo,md=8 , style={'background-color':'lightgray'}),
        dbc.Col (derecho,md=4 , style={'background-color':'lightblue'})
    ])

 ])