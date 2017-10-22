import os
import time
import threading
import mraa
from time import gmtime, strftime
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import requests

app = Flask(__name__)
class Clock(object):
	def __init__(self):
		self.alarm = False
		self.custom = False
		self.touch = mraa.Gpio(32)
		self.touch.dir(mraa.DIR_IN)
		
	def initthreads(self):
		thread1 = threading.Thread(target=self.update)
		thread1.start()
		thread2 = threading.Thread(target=self.Alarm)
		thread2.start()
		thread3 = threading.Thread(target=self.returnSnooze)
		thread3.start()

	def update(self):
		while True:
			if self.custom == False:
				a = strftime("%H:%M:%S %Y-%m-%d", gmtime()).replace(' ', '/')
				requests.post('http://192.168.43.239:8888/write/{}'.format(a))
			time.sleep(.5)

	def customText(self, text1, text2=" "):
		self.custom = True
		text1 = text1.replace(' ', '%20')
		text2 = text2.replace(' ', '%20')
		requests.post('http://192.168.43.239:8888/write/{}/{}'.format(text1, text2))

	def returnSnooze(self):
		while True:
			if self.alarm == True:
				time.sleep(1)
				if self.touch.read() == 0 and self.alarm == True:
					self.alarm = False

	def Alarm(self):
		while self.alarm == True:
			buzz = mraa.Gpio(29)
			buzz.dir(mraa.DIR_OUT)
			buzz.write(1)
			time.sleep(.5)
			buzz.write(0)
			time.sleep(.5)


	def startAlarm(self):
		self.alarm = True



