import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.H1('Sansty Dash', className='w3-center'),
    html.Article([
        html.Header(html.H2('Dash 示例', className='w3-center')),
        dcc.Link('callback context', href='/examples/flask-caching',
                 className='w3-padding'),
    ], className='w3-pale-blue w3-padding')
])
