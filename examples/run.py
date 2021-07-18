from examples import flask_caching


def callback_example(pathname):
    if pathname == '/examples/flask-caching':
        return flask_caching.layout
    else:
        return "Error"