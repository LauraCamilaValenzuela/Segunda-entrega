import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math

app = dash.Dash(__name__,external_stylesheets=[ dbc.themes.BOOTSTRAP])

from frontend.main import layout

app.layout = layout

@app.callback(
    Output('salidaPisos','children'),
    Input('entradaPisos','value'),
)
def numeroPisos(entradaPisos):
    if 1 <= entradaPisos <= 3:
        categoria = 'categoria baja'
        cargasMaximas = 'menores a 800 KN'
    elif 4 <= entradaPisos <= 10:
        categoria = 'categoria media'
        cargasMaximas = 'entre 801 y 4000 KN'
    elif 11 <= entradaPisos <= 20:
        categoria = 'categoria alta'
        cargasMaximas = 'entre 4001 y 8000 KN'
    elif entradaPisos >20:
        categoria = 'categoria especial'
        cargasMaximas = 'mayores a 4000 KN'
    else: 
        mensaje = 'Ingrese un dato valido'
    return 'EDIFICIO: ' + str(categoria) + ', las cargas máximas de servicio en las columnas son ' + str(cargasMaximas)

if __name__ == '__main__' :
    app.run_server(debug=True)