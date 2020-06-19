import dash, wolframalpha
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=external_stylesheets)
server = app.server

colors = {'background': '#ffffff', 'text': '#33B5FF'}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'color': colors['text'], 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px'}, 
	children=[
		html.Div([
			dcc.Input(id='input_ineqs', placeholder='Please input the inequalities separated by commas.', type='text', style={'width': '50%', 'display': 'inline-block'}),
			html.Button('Submit', id='submit_button'),
		]),
		html.Div([
			html.H3(id='output_area', style={'color': colors['text'], 'backgroundColor': colors['background']}),
			])
		])

def quad_ineq_solver(inequalities):
    appid= 'YRL93R-W2ATR8XGLX'
    client = wolframalpha.Client(appid)
    
    res = client.query(inequalities)

    solution_regions = []

    for i in range(len(res['pod'])):
        try:
            solution_regions.append(res['pod'][i]['subpod']['img']['@alt'])
        except:
            pass

    return list(set(solution_regions))

@app.callback(
	Output('output_area', 'children'),
	[Input('submit_button', 'n_clicks')],
	[State('input_ineqs', 'value')]
	)
def update_output(n_clicks, inequalities):
	if n_clicks:
		return quad_ineq_solver(inequalities)

if __name__ == '__main__':
	app.run_server(debug=True)