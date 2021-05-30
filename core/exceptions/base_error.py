class BaseError(object):
    def __init__(self):
        self.has_error = False
        self.global_error = {
            'has_error': False,
            'message': '',
            'data': ''
        }
