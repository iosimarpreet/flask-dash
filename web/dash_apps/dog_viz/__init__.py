import dash_html_components as html
import dash_core_components as dcc
from web.dash_apps import create_dash_layout

chart = dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Dog'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Dog 2'},
                    ],
                    'layout': {
                        'title': 'Dog Data Visualization'
                    }
                }
            )


chart_2 = dcc.Graph(
                id='example-graph-2',
                figure={
                    'data': [
                        {'x': [1, 43, 4, 31, 43, 2, 30, 2, 4, 3, 6, 7, 8, 6, 3, 0, 1, 5, 3], 'y': [31, 43, 42, 31, 43, 22, 33, 2, 4, 83, 26, 67, 48, 6, 32, 22, 41, 55, 31], 'type': 'bar', 'name': 'Dog'}
                    ],
                    'layout': {
                        'title': 'Dog Data Visualization 2.0'
                    }
                }
            )

viz = html.Div(children=[
    chart,
    chart_2
])

layout = create_dash_layout(viz)
