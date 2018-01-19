#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('Content-length', 0))

        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()

        # 3. Extract the "message" field from the request data.
            # Mike - my original answer is below on line 40, and the correct answer is on line 41.  
            #        So I am looking for a good book for either a reference or beginner book (I don't care 
            #        what it's called), that can explain the little nuances in python.  I could not find 
            #        any reference online or in the few books that I looked at that showed parse_qs() with a "["xyz"][0]"
            #        on the end and what that references to.  Hope that makes sense. But that is the type of thing 
            #        that I am taking HOURS trying to find and getting farther and farther behind.  Thanks again for any suggestions.
            
        # message = parse_qs(data) === this is my original answer
        message = parse_qs(data)["message"][0]
        
        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
