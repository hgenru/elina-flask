from flask import Flask, render_template


application = Flask('elinas_app')

@application.route("/")
def hello():
	return render_template('form.html')

if __name__ == "__main__":
    application.run()
