from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/command/')
def input():
	if request.args.get('command') == None:
		return render_template('linux.html')
	else:
		command = request.args['command']
		osResult = os.popen(command).read()
		return render_template('linux.html', result=osResult, cmd=command )

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
