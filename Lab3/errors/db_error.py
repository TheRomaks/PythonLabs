
class DBError(Exception):
    pass

class InvalidDBError(DBError):
    def __init__(self, message):
        super().__init__(message)