import pytest

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################

def test_index():
    """Test that the index page shows "Hello, World!" """
    res = app.test_client().get('/')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################

def test_color_results_blue():
    result = app.test_client().get('/color_results?color=blue')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, blue is my favorite color, too!'

    assert expected_page_text == result_page_text

def test_color_results_black():
    result = app.test_client().get('/color_results?color=black')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow! Black is my favourite colour as well!'
    assert expected_page_text == result_page_text

def test_color_results_empty():
    result = app.test_client().get('/color_results?color=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You did not specify your colour!"
    assert expected_page_text == result_page_text


#######################
# Froyo Tests
#######################

def test_froyo_results_scenario1():
    result = app.test_client().get('/froyo_results?flavour=chocolate&toppings=pistachio')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You ordered Chocolate flavoured Fro-Yo with toppings Pistachio!"
    assert expected_page_text == result_page_text

def test_froyo_results_scenario2():
    result = app.test_client().get('/froyo_results?flavour=2&toppings=1')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered 2 flavoured Fro-Yo with toppings 1!'
    assert expected_page_text == result_page_text

def test_froyo_results_edgecase1():
    result = app.test_client().get('/froyo_results?flavour=vanilla&toppings=strowberry')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered vanilla flavoured Fro-Yo with toppings strowberry!'
    assert expected_page_text == result_page_text

def test_froyo_results_edgecase2():
    result = app.test_client().get('/froyo_results?flavor=&toppings=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You did not specify a flavour and toppings!"
    assert expected_page_text == result_page_text

#######################
# Reverse Message Tests
#######################

def test_message_results_helloworld():
    form_data = {
        'message': 'Hello World'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'dlroW olleH' in result_page_text

def test_message_results_scenario2():
    form_data = {
        'message': "Hey! How are you?"
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "?uoy era woH !yeH" in result_page_text

def test_message_results_edgecase1():
    form_data = {
        'message': ""
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "Say something!" in result_page_text


#######################
# Calculator Tests
#######################

def test_calculator_results_scenario1():
    form_data = {
        'operand1': '2',
        'operand2': '2',
        'operation': 'add'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to add 2 and 2. Your result is: 4' in result_page_text

def test_calculator_results_scenario2():
    form_data = {
        'operand1': '-2',
        'operand2': '-4',
        'operation': 'subtract'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to subtract -2 and -2. Your result is: 0' in result_page_text

def test_calculator_results_scenario3():
    form_data = {
        'operand1': '2',
        'operand2': '4',
        'operation': 'multiply'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to multiply 2 and 2. Your result is: 4' in result_page_text

def test_calculator_results_scenario4():
    form_data = {
        'operand1': '2',
        'operand2': '4',
        'operation': 'devide'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to devide 2 and 2. Your result is: 1' in result_page_text

def test_calculator_results_edgecase1():
    form_data = {
        'operand1': 2,
        'operand2': 4,
        'operation': 'add'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to add 2 and 2. Your result is: 4' in result_page_text

def test_calculator_results_edgecase2():
    form_data = {
        'operand1': '',
        'operand2': '',
        'operation': ''
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "Please enter two numbers and an operation." in result_page_text
