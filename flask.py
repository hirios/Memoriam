from flask import Flask, render_template


app = Flask(__name__)
@app.route('/<complemento>/<outro>')
def home(complemento, outro):
    return complemento + " " + outro

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

