#!/usr/bin/env python


from influxdb import InfluxDBClient
import web


urls = (
	'/getTemperature', 'getTemperature',
	'/getHumidity', 'getHumidity'
)

influx_client = InfluxDBClient('influxdb', 8086, database='balena-sense')

class getTemperature:
	def GET(self):
		result = influx_client.query('SELECT ( last("temperature") ) FROM "balena-sense"')
		res = result.items()[0][1]
		for r in res:
			return r['last']
		
		# default to blank
		return ''

class getHumidity:
	def GET(self):
		result = influx_client.query('SELECT ( last("humidity") ) FROM "balena-sense"')
		res = result.items()[0][1]
		for r in res:
			return r['last']
		
		# default to blank
		return ''


if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()