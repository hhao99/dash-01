from dash import Dash, dcc, html,Input,Output, callback
import plotly.express as px

app = Dash(__name__)
title = 'Canada New Housing Price Indexes'
app.layout = html.Div([
    html.H1(title),
    dcc.Graph(figure={},id='graph'),
    dcc.RadioItems(options=df['geo'].unique(),id='radio-item-1')
])

@callback(
    Output(component_id='graph',component_property='figure'),
    Input(component_id='radio-item-1',component_property='value')
)
def update(geo_chosen):
    fig = px.histogram(
        df[df['geo']== geo_chosen],
        x='ref_date',
        y='value',
        histfunc='avg'
    )
    
    return fig


app.run(debug=True)