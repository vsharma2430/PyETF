import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandas import DataFrame
from datetime import datetime

def get_simple_chart(df:DataFrame):
        fig = df.plot(backend='plotly')
        return fig.to_html(full_html=False)

def get_chart(df:DataFrame):
    # Create subplots and mention plot grid size
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'), 
                row_width=[0.2, 0.7])

    # Plot OHLC on 1st row
    #datetime.fromtimestamp(dd).strftime('%c')
    dates = [datetime.fromtimestamp(dd/1000000000) for dd in df.index.values.tolist()]

    fig.add_trace(go.Candlestick(x=dates,open=df["Open"], high=df["High"],
                    low=df["Low"], close=df["Close"], name="OHLC"), 
                    row=1, col=1
    )

    # Bar trace for volumes on 2nd row without legend
    fig.add_trace(go.Bar(x=dates,y=df['Volume'], showlegend=False), row=2, col=1)

    # Do not show OHLC's rangeslider plot 
    fig.update(layout_xaxis_rangeslider_visible=False)

    return fig.to_html(full_html=False)

def get_chart_with_volume(df:DataFrame):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # include candlestick with rangeselector
    fig.add_trace(go.Candlestick(
                    open=df['Open'], high=df['High'],
                    low=df['Low'], close=df['Close']),
                secondary_y=True)

    # include a go.Bar trace for volumes
    fig.add_trace(go.Bar(y=df['Volume']),
                secondary_y=False)

    fig.layout.yaxis2.showgrid=False

    return fig.to_html(full_html=False)