import os
import time
import threading
from time import gmtime, strftime
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify


'''class Clock(object):
	def __init__(object):
		strftime("%Y-%m-%d %H:%M:%S", gmtime())'''




@app.route('/clear/', methods=['POST'])
def clear():
	os.system('sudo ./clear')

@app.route('/write/<text>', methods=['POST'])
def write():
	text = text.split("/")
	text = text.join(' ')
	os.system('sudo ./main {}'.format(text))


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)