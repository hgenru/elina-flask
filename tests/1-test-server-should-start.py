from nose.tools import eq_
from app.server import application

APP = application.test_client()

def test_server_should_return_ok():
    response = APP.get('/')
    status_code = response.status_code
    eq_(
        status_code, 200,
        msg="Server should return 200 OK on /, not {0}".format(status_code)
    )
