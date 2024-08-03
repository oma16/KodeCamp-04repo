 import os
 from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Define the response status code and headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Read the welcome message from an environment variable
        welcome_message = os.getenv('WELCOME_MESSAGE', 'Hello, Welcome to KodeCamp DevOps Bookcamp!')
        # Write the response message
        
        response_message = "<html><body><h1>{welcome_message}</h1></body></html>"
        self.wfile.write(response_message.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()



def main():
    
    run()
    
    
    
main()