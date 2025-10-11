from flask import Flask, request

app = Flask(__name__)

balance = 0

@app.route('/mybank/')
def deposit():
	if request.method != 'GET':
		return ""
	global balance
	if request.args.get('deposit') != None:
		deposit = request.args['deposit']
		depositMoney = int(deposit)
		balance += depositMoney
		return "<h2>입금 %d원, 잔액 %d</h2>" %(depositMoney, balance)	
	elif request.args.get('withdraw') != None:
		withdraw = request.args['withdraw']
		withdrawMoney = int(withdraw)
		withdrawMoney = balance if balance < withdrawMoney else withdrawMoney
		balance -= withdrawMoney
		return "<h2>출금 %d원, 잔액 %d</h2>" %(withdrawMoney, balance)	
	elif request.args.get('inquiry') != None:
		return "<h2>잔액 %d</h2>" %(balance)
	else:
		return "입금, 출금, 잔액조회 중 하나를 입력하세요."
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

