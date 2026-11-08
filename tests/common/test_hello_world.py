from common.hello_world import greeting


def test_greeting_uses_the_provided_name():
    assert greeting("architect") == "Hello, architect!"

