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
        
        # Read the database password from an environment variable
        db_password = os.getenv('DB_PASSWORD', 'default_password')
        
        # Write the response message
        
        response_message = f"<html><body><h1>Hello, Welcome to KodeCamp DevOps Bookcamp!</><h1>{welcome_message}</h1><p>DB Password Length: {len(db_password)}</p></body></html>"
        self.wfile.write(response_message.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()



def main():
    
    run()
    
    
    
main()