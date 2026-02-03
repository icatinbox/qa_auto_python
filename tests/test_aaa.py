import pytest

def test_summ_aaa():
    #arrange. Подготовка данных
    a = 2
    b = 15

    #act. Действие
    result = a + b

    #assert. Проверили результат
    assert result == 17

@pytest.mark.smoke
def test_have_name(user_data):
    assert 'name' in user_data
    assert user_data['name'] == 'Ivan'

@pytest.mark.smoke
def test_have_age(user_data):
    assert 'age' in user_data
    assert user_data['age'] >= 18