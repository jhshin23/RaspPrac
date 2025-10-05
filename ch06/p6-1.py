from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<float:op1>/<op>/<float:op2>/')
def calc(op1, op, op2):
	return render_template('p6-1.html', op1 = op1, op = op, op2 = op2)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 8080, debug = True)
