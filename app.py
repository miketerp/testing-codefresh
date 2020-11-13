import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
app.title = 'Hello peter17'
server = app.server

app.layout = html.Div([
    html.H1("TESTING DEPLOYMENT"),
    html.P("hello peter 17"),
    html.P("testing")
])


if __name__ == '__main__':
    app.run_server(debug=True)
