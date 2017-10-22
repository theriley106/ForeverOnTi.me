import os
import time
import threading
from time import gmtime, strftime
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import mraa
import clock
app = Flask(__name__)
'''class Clock(object):
	def __init__(object):
		strftime("%Y-%m-%d %H:%M:%S", gmtime())'''

touch = mraa.Gpio(32)
touch.dir(mraa.DIR_IN)
clock = clock.Clock()

@app.route('/clear/', methods=['POST'])
def clear():
	os.system('sudo ./clear')
	return redirect(url_for('index'))

@app.route('/write/<text1>', methods=['POST'])
@app.route('/write/<text1>/<text2>', methods=['POST'])
def write(text1, text2=""):
	print text1
	print text2
	os.system('sudo ./main "{}" "{}"'.format(text1, text2))
	return redirect(url_for('index'))

@app.route('/alarm/start', methods=['POST'])
def alarm():
	clock.startAlarm()
	return redirect(url_for('index'))

@app.route('/alarm/snooze', methods=['POST'])
def snooze():
	clock.alarm = False
	return redirect(url_for('index'))


@app.route('/alarm/addvar/<times>', methods=['POST'])
def alarmSetting(times):
	time1, time2 = times.split('+')
	clock.setAlarm(time1, time2)
	return redirect(url_for('index'))

@app.route('/alarm/off', methods=['POST'])
def turnOff():
	clock.clear()
	return redirect(url_for('index'))

@app.route('/alarm/on', methods=['POST'])
def turnOn():
	clock.turnOn()
	return redirect(url_for('index'))

@app.route('/convertSet', methods=['POST'])
def convertSet():
	items = request.form.items()
	start = items[0][1]
	end = items[1][1]
	return redirect(url_for('alarmSetting', times="+".join(start,end)))

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	clock.initthreads()
	app.run(host='0.0.0.0', port=8888, debug=True)
