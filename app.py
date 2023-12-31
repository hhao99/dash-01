from dash import Dash, html, dash_table
# import plotly.express as px
import pandas as pd 

url = './housing.parquet'
df = pd.read_parquet(url)
title = 'Canada Housing Statistics'

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children= title),
    dash_table.DataTable(data=df.to_dict('records'),page_size=10)
]);
if __name__ == '__main__':
    app.run(debug=True)