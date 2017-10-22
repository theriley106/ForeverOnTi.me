import requests
import json
import os


def js_r(filename):
	with open(filename) as f_in:
   		f_in = '{' + str(f_in.read()).partition('{')[2].strip()
    	return(json.loads(f_in))


def getSleep(curl='curl -i -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzU0s2RlYiLCJhdWQiOiIyMkNKRFAiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNTA5MjYyOTQ0LCJpYXQiOjE1MDg2NTgxNjh9.J63wQUZF0HOAhgk2e0r7fBm610VZJ3wJ0u6YZ5UJxkA" https://api.fitbit.com/1.2/user/-/sleep/date/2017-10-22.json')
	os.system(curl + ' > t.json')
	a = js_r('t.json')
	if len(a['sleep']) == 0:
		print("You should get some sleep")
		#this implies that you haven't slept yet today
		#for presentation we will use test data set from fitbit
		a = js_r('test.json')
		return a['sleep'][0]['levels']['shortData'][0]['level']
	else:
		return a['sleep'][0]['levels']['shortData'][0]['level']