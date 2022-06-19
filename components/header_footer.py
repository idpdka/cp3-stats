from dash import html, dcc

def generate_header():
    return [
        html.H1(
            children='Cendana Peak'
        ),

        html.H2(
            children='The Statistics'
        ),

        html.Div(
            children='Dashboard ini berisi informasi statistik mengenai keberjalanan proyek Cendana Peak di Lippo Karawaci.'
        ),

        html.Div(
            children='* data didapatkan dari pengumpulan informasi oleh calon penghuni dan penghuni Cendana Peak 3. Mohon digunakan dengan bijak.',
        ),
    ]

def generate_footer():
    return [
        html.Br(),
        html.Br(),
        dcc.Markdown(children=
            '''
                Built with love in Python using [Dash](https://plotly.com/dash/)
            ''',
        ),
    ]