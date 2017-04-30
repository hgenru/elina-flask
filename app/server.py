import os
from flask import Flask, render_template

application = Flask("elina's server")  # pylint: disable=invalid-name
application.debug = True

@application.route('/')
def handle_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=PORT)
