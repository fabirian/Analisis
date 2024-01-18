import yfinance as yf
import plotly.graph_objects as go

def descargar_datos(empresa, inicio, fin):
    return yf.download(empresa, start=inicio, end=fin)

def crear_grafico_velas(df, titulo):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['Open'], high=df['High'],
                    low=df['Low'], close=df['Adj Close'],
                    text=df['Retorno'].apply(lambda x: f"Retorno: {x:.2f}"))])

    fig.update_layout(title=titulo,
                      xaxis_title="Fecha",
                      yaxis_title="Precios")

    return fig

