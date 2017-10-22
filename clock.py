import os
import time
import threading
import mraa
from time import gmtime, strftime
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import requests
from pytz import timezone
import pytz
from datetime import datetime, timedelta
app = Flask(__name__)
class Clock(object):
	def __init__(self):
		self.alarm = False
		self.custom = False
		self.touch = mraa.Gpio(32)
		self.touch.dir(mraa.DIR_IN)
		self.baseSnooze = self.touch.read()
		
	def initthreads(self):
		thread1 = threading.Thread(target=self.update)
		thread1.start()
		thread2 = threading.Thread(target=self.Alarm)
		thread2.start()
		thread3 = threading.Thread(target=self.returnSnooze)
		thread3.start()

	def update(self):
		time.sleep(3)
		eastern = timezone('US/Eastern')
		fmt = '%Y-%m-%d %H:%M:%S'
		while True:
			if self.custom == False:
				#a = strftime("%H:%M:%S %Y-%m-%d", gmtime()).replace(' ', '/')
				loc_dt = eastern.localize(datetime(2012, 10, 29, 6, 0, 0))
				a = loc_dt.strftime(fmt)
				a, b = a.split(' ')
				os.system('sudo ./main "{}" "{}"'.format(a, b))
			time.sleep(.8)

	def customText(self, text1, text2=" "):
		self.custom = True
		text1 = text1.replace(' ', '%20')
		text2 = text2.replace(' ', '%20')
		requests.post('http://192.168.43.239:8888/write/{}/{}'.format(text1, text2))

	def returnSnooze(self):
		time.sleep(3)
		while True:
			if self.alarm == True:
				if self.touch.read() != self.baseSnooze:
					self.alarm = False
					print("Alarm STOPPED")

	def Alarm(self):
		time.sleep(3)
		while True:
			if self.alarm == True:
				buzz = mraa.Gpio(29)
				buzz.dir(mraa.DIR_OUT)
				buzz.write(1)
				time.sleep(.5)
				buzz.write(0)
				time.sleep(.5)


	def startAlarm(self):
		self.alarm = True



