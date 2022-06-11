from python_pkg import greeting


def test_hello_no_name():
    assert greeting.say_hello() == 'Hello!'


def test_hello_name():
    assert greeting.say_hello(name='ChopChop') == 'Hello ChopChop!'


def test_hi_no_name():
    assert greeting.say_hi() == 'Hi!'


def test_hi_name():
    assert greeting.say_hi(name='ChopChop') == 'Hi ChopChop!'
