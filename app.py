# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df_table = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Cendana Peak 3',
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
            Dashboard ini berisi informasi statistik mengenai keberjalanan proyek Cendana Peak 3 di Lippo Karawaci.
        ''',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='''
            * data didapatkan dari pengumpulan informasi oleh calon penghuni dan penghuni Cendana Peak 3. Mohon digunakan dengan bijak.
        ''',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    generate_table(df_table)
])

if __name__ == '__main__':
    app.run_server(debug=True)