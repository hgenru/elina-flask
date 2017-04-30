import os
from flask import Flask, request, render_template

application = Flask("elina's server")  # pylint: disable=invalid-name
application.debug = True

@application.route('/', methods=['GET'])
def handle_index_page():
    return render_template('index.html')

@application.route('/calculate', methods=['POST'])
def handle_calculate():
    form_data = request.form
    number_one = int(form_data['number_one'])
    number_two = int(form_data['number_two'])
    numbers_sum = number_one + number_two
    return render_template('calculate.html', result=numbers_sum)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=PORT)
