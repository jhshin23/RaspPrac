from flask import Flask
app = Flask(__name__)

@app.route('/<op1>/<op>/<op2>/')
def calc(op1, op, op2):
	if op == 'plus':
		return "<h2>%f + %f = %f</h2>" %(float(op1),float(op2), float(op1)+float(op2))
	elif op == 'minus':
		return "<h2>%f - %f = %f</h2>" %(float(op1), float(op2), float(op1)-float(op2))
	elif op == 'multiply':
		return "<h2>%f * %f = %f</h2>" %(float(op1), float(op2), float(op1)*float(op2))
	elif op == 'divide':
		if op2 == '0':
			return "0으로 나눌 수 없습니다."
		return "<h2>%f / %f = %f</h2>" %(float(op1), float(op2), float(op1)/float(op2))
	else:
		return "없는 연산자입니다."

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

