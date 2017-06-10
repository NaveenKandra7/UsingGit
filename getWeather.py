#!/usr/python

import requests
import pdb

#print "I am in the file"

def main(city) :
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&Appid=dd41d47b420e1b2a8b8831016969eb41&units=metric')
	output = response.json()
	#pdb.set_trace()
	#print "after pdb"
	temperature = output['main']['temp']
	print temperature
	print output['sys']['country']
if __name__ == "__main__":
	main('Bangalore')
