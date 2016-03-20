from v1 import api


@api.route('/auth', methods=['GET', 'POST'])
def auth_index():
    return "<h1>Hello from AUTH</h1>"


@api.route('/auth/token')
def token():
    pass
