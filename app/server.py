from flask import Flask, render_template, request, redirect


application = Flask('elinas_app')

@application.route("/", methods=['POST'])
def input_data():
	return render_template('form.html')


@application.route("/calculate", methods=['GET','POST'])
def calculate():
	number_one = int(request.form.get('number_one'))
	number_two = int(request.form.get('number_two'))
	sum_one_two = int(number_one + number_two)
	return render_template ('result.html', sum_one_two=sum_one_two)

if __name__ == "__main__":
    application.run(debug=True)
