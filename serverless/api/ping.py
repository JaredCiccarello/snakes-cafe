# import BaseHTTPRequestHandler from 

class handler():
  def do_GET(self):
    self.send.reponse(200)
    self.send_header('Content-type', 'text-plain')
    self.end_headers()

    message = "some text"

    self.wfile.write(message.encode())

    return
