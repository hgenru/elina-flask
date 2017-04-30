from nose.tools import ok_, eq_
from app.server import application
from tests.utils import parse_dom, get_element_by_xpath

APP = application.test_client()

def get_form(response_data):
    dom = parse_dom(response_data)
    return get_element_by_xpath(dom, '//form')


def test_server_should_return_form():
    response = APP.get('/')
    form_element = get_form(response.data)
    ok_(form_element is not None, msg="Form element should exist on page")

def test_server_should_return_form_with_method_post():
    response = APP.get('/')
    form_element = get_form(response.data)
    form_method = form_element.get('method')
    eq_(form_method, 'POST', msg="Form element should have attr method=POST")

def test_server_should_return_form_with_action_calculate():
    response = APP.get('/')
    form_element = get_form(response.data)
    form_action = form_element.get('action')
    eq_(form_action, '/calculate', msg="Form element should have attr action=/calculate")

def test_server_should_return_input_for_number_one():
    response = APP.get('/')
    dom = parse_dom(response.data)
    input_one = get_element_by_xpath(dom, '//form//input[@name="number_one"]')
    ok_(input_one is not None, msg="Input for number one (name=number_one)")

def test_server_should_return_input_for_number_two():
    response = APP.get('/')
    dom = parse_dom(response.data)
    input_two = get_element_by_xpath(dom, '//form//input[@name="number_two"]')
    ok_(input_two is not None, msg="Input for number two (name=number_two)")
