from dash import html, dcc

def generate_header(colors):
    return [
        html.H1(
            children='Cendana Peak',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.H2(
            children='The Statistics',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(
            children='''
                Dashboard ini berisi informasi statistik mengenai keberjalanan proyek Cendana Peak di Lippo Karawaci.
            ''',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
    ]

def generate_footer(colors):
    return [
        html.Br(),
        html.Br(),
        dcc.Markdown(
            children='''
                Built with love in Python using [Dash](https://plotly.com/dash/)
            ''',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
    ]