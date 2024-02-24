
def say_hello(name=None):
    """
    Function that returns a simple greeting starting with "Hello"
    an optional `name` parameter can be provided to personalize
    the greeting

    :param name: optional name to personalize greeting
    :type name: str
    """
    if name is not None:
        return f'Hello {name}!'

    return 'Hello!'


def say_hi(name=None):
    """
    Function that returns a simple greeting starting with "Hi"
    an optional `name` parameter can be provided to personalize
    the greeting

    :param name: optional name to personalize greeting
    :type name: str
    """
    if name is not None:
        return f'Hi {name}!'

    return 'Hi!'
