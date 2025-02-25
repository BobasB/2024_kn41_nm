from program.main import new_fun


def test_for_pytest():
    assert True, "Тут завжди має бути істина"
    assert 1 != 2, "Тут проста перевірка"

def test_new_fun():
    assert new_fun() == 50, "Неправиильно певернуте значення"
