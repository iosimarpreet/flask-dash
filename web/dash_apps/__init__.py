import dash_html_components as html

navigation_bar =html.Nav(className="navbar", children=[
        html.Div(className="navbar-menu", children=[
            html.Div(className="navbar-end", children=[
                html.A("Home", className="navbar-item", href='/'),
                html.A("DogViz", className="navbar-item", href='/dogs/dog_viz/'),
                html.A("CatViz", className="navbar-item", href='/cats/cat_viz/')
            ])
        ])
    ])

header = html.Div(
    children=[
        html.H1(className="title", children="PetApp"),
        html.P(className="subtitle", children="A one-stop-shop for all pet related tech.")
    ]
)


def create_dash_layout(dash_content):
    app_layout = html.Div(children=[
        html.Div(className="section", children=[
            navigation_bar,
            header,
            html.Div(className="container", children=[
                dash_content
            ])
        ])
    ])
    return app_layout


