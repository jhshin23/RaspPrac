from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/editor/')
def edit():
	if os.path.isfile("memo.txt"):
		file = open("memo.txt", "r")
		oldMemo = ""
		for line in file.readlines():
			oldMemo += line	
		return render_template('editor.html', memo=oldMemo)
	else:
		return render_template('editor.html', memo="")
		
@app.route('/editor/', methods=['POST'])
def saveMemo():
	memo = request.form['memo']
	file = open("memo.txt", "w")
	file.write(memo)
	file.close()
	
	return "<h2>memo.txt 파일에 저장되었습니다.</h2>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)

