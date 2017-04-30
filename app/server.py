import os
from flask import Flask

application = Flask("elina's server")  # pylint: disable=invalid-name

@application.route("/")
def handle_index_page():
    return "Hello World"

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=PORT)
