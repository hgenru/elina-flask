from flask import Flask, render_template, request, redirect


application = Flask('elinas_app')

#application - это декоратор (модификатор функции, функция для функции)
#синтаксический сакр - одной функции передала другой функции
#в декораторе route функция начала обрабатывать урлы
@application.route("/", methods=['GET'])
def input_data():
	return render_template('form.html')

#запрос GET - «Дай мне что-то». POST — «Создай что-то»
#Постом обязательно делаются конфид данные (например, пароли или сообщения
#чтобы не видно было в урле)
@application.route("/calculate", methods=['POST'])
def calculate():
	number_one = int(request.form.get("number_one"))
	number_two = int(request.form.get("number_two"))
	sum_one_two = int(number_one + number_two)
	return render_template ('result.html', sum_one_two=sum_one_two)

if __name__ == "__main__":
    application.run(debug=True)
