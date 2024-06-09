class StoreException(Exception):
    pass

class RedoException(StoreException):
    pass

class UndoException(StoreException):
    pass
