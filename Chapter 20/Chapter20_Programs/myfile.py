class Error(Exception):
    '''Base class for all the exceptions raised in this application'''


class DatabaseError(Error):
    pass


class NetworkError(Error):
    pass


class InvalidInputError(Error):
    pass


class HostnameNotResolvedError(NetworkError):
    pass


class ProtocolFailedError(NetworkError):
    pass


class ConnectionClosedError(NetworkError):
    pass


class NetworkChangedError(NetworkError):
    pass


class AddressNotReachableError(NetworkError):
    pass


class InvalidNumberError(InvalidInputError):
    pass


class InvalidAlphabetError(InvalidInputError):
    pass


class NegativeNumberError(InvalidNumberError):
    pass


class OutOfRangeError(InvalidNumberError):
    pass


class InvalidCursorError(DatabaseError):
    pass


class NoDataFoundError(DatabaseError):
    pass


class StorageError(DatabaseError):
    pass


def func1():
    print('func1 called')
    raise InvalidCursorError


def func2():
    print('func2 called')
    raise NetworkError
