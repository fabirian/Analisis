# src/app.py
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import yfinance as yf
import numpy as np
import pandas as pd
from src import analisis, prediccion

# Descargar datos de Yahoo Finance
df = yf.download('GOOG', start='2018-01-01', end='2023-07-30')

# Crear la aplicación Dash
app = Dash(__name__)

# Crear el diseño de la aplicación
app.layout = html.Div(
    [
        html.H4("Google stock candlestick chart"),
        dcc.Checklist(
            id="toggle-rangeslider",
            options=[{"label": "Include Rangeslider", "value": "slider"}],
            value=["slider"],
        ),
        dcc.Graph(id="graph"),
    ]
)

# Callback para actualizar el gráfico
@app.callback(
    Output("graph", "figure"),
    Input("toggle-rangeslider", "value"),
)
def display_candlestick(value):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Adj Close'])])
    fig.update_layout(xaxis_rangeslider_visible="slider" in value)
    return fig

# Iniciar la aplicación si se ejecuta como script principal
if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050)


