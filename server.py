#!/usr/bin/env python
import os
import time
import BaseHTTPServer

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def resp(self, data, mime="text/html"):
		self.send_response(200) # or somting else
		self.send_header("Content-type", mime) # default is html/text
		self.end_headers()
		self.wfile.write(data) # write the data. (Close connection?)
	
	def do_GET(self):

		path = self.path[1:]
		if len(path) == 0: return self.resp(open('index.html').read())
		elif os.path.exists(path): return self.resp(open(path).read())
		else: return self.resp("BAD CALL")
	
	def do_POST(self):
		return self.resp("POST CALL")


if __name__ == '__main__':
	HOST_NAME = ''
	PORT_NUMBER = 80

	server_class = BaseHTTPServer.HTTPServer 
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
	try:
		httpd.serve_forever()
	except:
		print('ERROR: ' + e)
	httpd.server_close()
	print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
