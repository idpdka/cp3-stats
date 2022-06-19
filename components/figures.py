from dash import dcc, dash_table
import dash_bootstrap_components as dbc
import pandas.io.sql as sqlio
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib as mpl

# Figures
def generate_overall_handover_status_pie(conn, colors):
    query = """
        SELECT
            CASE
                WHEN handover_at IS NOT NULL THEN 'Sudah Handover'
                WHEN handover_at IS NULL AND updated_at IS NOT NULL THEN 'Belum Handover'
                ELSE 'Belum Lapor'
            END as handover_status,
            COUNT(id) as count
        FROM
            unit
        GROUP BY
            handover_at, updated_at
    """

    df = sqlio.read_sql_query(query, conn)
    fig = px.pie(df, values='count', names='handover_status', title='Status Handover Keseluruhan')

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return dcc.Graph(
        id='overall-handover-status',
        figure=fig
    )

def generate_per_subcomplex_handover_status_pie(conn, colors):
    query = """
        SELECT
            subcomplex.id,
            subcomplex.code,
            CASE
                WHEN unit.handover_at IS NOT NULL THEN 'Sudah Handover'
                WHEN unit.handover_at IS NULL AND unit.updated_at IS NOT NULL THEN 'Belum Handover'
                ELSE 'Belum Lapor'
            END as handover_status,
            COUNT(unit.id) as count
        FROM
            unit LEFT JOIN subcomplex
                ON unit.subcomplex_id = subcomplex.id
        GROUP BY
            unit.handover_at, unit.updated_at, subcomplex.id, subcomplex.code
        ORDER BY
            subcomplex.id
    """

    df = sqlio.read_sql_query(query, conn)
    fig = px.bar(df, x='code', y='count', color='handover_status', title="Status Handover berdasarkan Sub-Complex")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return dcc.Graph(
        id='per-subcomplex-handover-status',
        figure=fig
    )

# Tables
def generate_table(style, conn, page_size=25):
    query = """
        SELECT
            subcomplex.code AS "Nomor Jalan",
            unit.unit_no AS "Nomor Rumah",
            unit.owner_name AS "Nama Owner",
            unit.co_owner_name AS "Nama Co-Owner",
            unit.phone_no AS "Nomor Telepon",
            CASE
                WHEN unit.handover_at IS NOT NULL THEN 'Sudah Handover'
                WHEN unit.handover_at IS NULL AND unit.updated_at IS NOT NULL THEN 'Belum Handover'
                ELSE 'Belum Lapor'
            END AS "Status Handover",
            unit.handover_at AS "Tanggal Handover"
        FROM
            unit LEFT JOIN subcomplex
                ON unit.subcomplex_id = subcomplex.id
    """
    df = sqlio.read_sql_query(query, conn)

    return dbc.Container([
        dbc.Label('Data Penghuni Cendana Peak', style=style['label']),
        dash_table.DataTable(
            style_header=style['header'],
            style_data=style['data'],
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            page_size=page_size,
            filter_action="native",
            sort_action="native",
            css=[
                {
                    'selector': '.page-number',
                    'rule': f"color: {style['label']['color']};"
                },
            ],
        ),
    ])

# Sample Figures
def generate_sample_bar_chart(colors):
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return dcc.Graph(
        id='example-graph',
        figure=fig
    )
