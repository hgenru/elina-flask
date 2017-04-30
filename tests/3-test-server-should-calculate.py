from nose.tools import ok_, eq_
from app.server import application
from tests.utils import parse_dom, get_element_by_xpath

APP = application.test_client()

def test_server_should_return_ok_on_calculate():
    response = APP.post('/calculate', data=dict(number_one=2, number_two=2))
    eq_(
        response.status_code, 200,
        msg="Server should return 200 OK on POST /calculate (got {0})".format(response.status_code)
    )

def test_server_should_calculate_2_plus_2():
    response = APP.post('/calculate', data={'number_one': 2, 'number_two': 2})
    dom = parse_dom(response.data)
    body_element = get_element_by_xpath(dom, '//body')
    body_text = "".join([x for x in body_element.itertext()])
    ok_('4' in body_text, msg="Result should be on page")
