# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash_bootstrap_components as dbc
import gunicorn
from dash import Dash, callback, html
from whitenoise import WhiteNoise
from components.header_footer import generate_header, generate_footer
from components.figures import generate_sample_bar_chart, generate_table

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

def create_dash_layout(app):
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    
    # Set browser tab title
    app.title = "Cendana Peak Statistics" 
    
    # Header
    header = html.Div(style={'textAlign': 'center', 'color': colors['text']}, children=generate_header())
    
    # Body 
    body = html.Div([
        generate_sample_bar_chart(colors),
        generate_table({'textAlign': 'center', 'color': colors['text']})
    ])

    # Footer
    footer = html.Div(style={'textAlign': 'center', 'color': colors['text']}, children=generate_footer())
    
    # Assemble dash layout 
    app.layout = html.Div(style={'textAlign': 'center', 'backgroundColor': colors['background']}, children=[header, body, footer])

    return app

create_dash_layout(app)

if __name__ == '__main__':
    app.run_server(debug=True)