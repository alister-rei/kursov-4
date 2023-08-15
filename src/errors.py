# Классы для ошибок

class MissingKeysException(Exception):
    def __init__(self, missing_keys):
        self.missing_keys = missing_keys
        super().__init__()


class ParsingError(Exception):
    def __init__(self, key_error):
        self.key_error = key_error
        super().__init__()
