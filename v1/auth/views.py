from v1 import api


@api.route('/auth')
def auth_index():
    return "hello from auth"
