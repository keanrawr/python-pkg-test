
def say_hello(name=None) -> str:
    '''
    Return a simple 'hello' greeting.

    :param name: Optional name to address the greeting to
    :type name: str or None
    :return: A string with a hello greeting
    :rtype: str
    '''
    if name is not None:
        return f'Hello {name}!'

    return 'Hello!'


def say_hi(name=None) -> str:
    '''
    Return a simple 'hi' greeting.

    :param name: Optional name to address the greeting to
    :type name: str or None
    :return: A string with a hi greeting
    :rtype: str
    '''
    if name is not None:
        return f'Hi {name}!'

    return 'Hi!'
