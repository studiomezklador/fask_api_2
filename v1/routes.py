from . import api, g, versions, Response, Json as j


@api.route('/')
def index():
    """
    if no browser and no platform: it's a CLI request.
    """
    if g.client['browser'] is None or g.client['platform'] is None:
        string = "hello from API {} -- in CLI Mode"
        msg = {'message': string.format(versions[0]),
               'status': 'OK',
               'mode': 200}
        r = Response(j.output(msg))
        r.headers['Content-type'] = 'application/json; charset=utf-8'
        return r, 200

    """
    ELSE: it's obviously on a web browser
    """
    string = "<h1>hello from API v1 | {} | {} | {} | {}</h1>"
    return string.format(g.client['browser'],
                         g.client['platform'],
                         g.client['version'],
                         g.client['language'])
