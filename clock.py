import os
import time
import threading
from time import gmtime, strftime
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import requests

app = Flask(__name__)
class Clock(object):
	def __init__(object):
		print strftime("%Y-%m-%d %H:%M:%S", gmtime())



a = Clock()
