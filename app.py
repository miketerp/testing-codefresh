import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
app.title = 'Hello peter9'
server = app.server

app.layout = html.Div([
    html.P("hello peter 9")
])


if __name__ == '__main__':
    app.run_server(debug=True)
