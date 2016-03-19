from v1 import api

@api.route('/auth')
def auth_index():
    return "<h1>Hello from AUTH</h1>"
