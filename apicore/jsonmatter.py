import simplejson as json


class Json(object):
    def __init__(self):
        pass

    @staticmethod
    def output(items, excluded=None):
        if excluded:
            for el in excluded:
                del items[el]
        return json.dumps(items)

    @staticmethod
    def input(items):
        return json.loads(items)
