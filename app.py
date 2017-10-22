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
	return "Done"

@app.route('/write/<text1>', methods=['POST'])
@app.route('/write/<text1>/<text2>', methods=['POST'])
def write(text1, text2=""):
	print text1
	print text2
	os.system('sudo ./main "{}" "{}"'.format(text1, text2))
	return "Done"

@app.route('/alarm/start', methods=['POST'])
def alarm():
	clock.startAlarm()
	return "DONE"

@app.route('/alarm/snooze', methods=['POST'])
def snooze():
	clock.alarm = False
	return "DONE"


@app.route('/alarm/addvar/<times>', methods=['POST'])
def alarmSetting(times):
	time1, time2 = times.split('+')
	clock.setAlarm(time1, time2)
	return "DONE"


if __name__ == "__main__":
	clock.initthreads()
	app.run(host='0.0.0.0', port=8888, debug=True)
